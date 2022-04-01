from math import pow
from math import radians

from femtomes_ros_driver.msg import FemtomesBESTXYZ
from femtomes_ros_driver.msg import FemtomesHEADING
from geometry_msgs.msg import Quaternion
import message_filters
from nav_msgs.msg import Odometry
import rospy
import tf
from tf.transformations import quaternion_from_euler


class FemtomesPublisher(object):
    def __init__(self, xyz_topic: str, heading_topic: str) -> None:
        self.publisher = rospy.Publisher(
            "femtomes/odom", Odometry, queue_size=1
        )
        self.publish_tf = rospy.get_param("~publish_tf", False)
        self.odom_frame = rospy.get_param("~odom_frame", "femtomes_odom")
        self.base_frame = rospy.get_param("~base_frame", "base_link")
        self.seq = 0
        if self.publish_tf:
            self.tf_broadcast = tf.TransformBroadcaster()
        sub_xyz = message_filters.Subscriber(
            "/femtomes/" + xyz_topic, FemtomesBESTXYZ
        )
        sub_heading = message_filters.Subscriber(
            "/femtomes/" + heading_topic, FemtomesHEADING
        )
        sync = message_filters.ApproximateTimeSynchronizer(
            [sub_xyz, sub_heading], 1000, 0.1
        )

        sync.registerCallback(self.publish)

    def publish(
        self, bestxyz: FemtomesBESTXYZ, heading: FemtomesHEADING
    ) -> None:
        odom = Odometry()
        odom.header.seq = self.seq
        odom.header.frame_id = self.odom_frame
        odom.header.stamp = (bestxyz.header.stamp + heading.header.stamp) / 2
        odom.child_frame_id = self.base_frame

        odom.pose.pose.position.x = bestxyz.p_x
        odom.pose.pose.position.y = bestxyz.p_y
        odom.pose.pose.position.z = bestxyz.p_z
        odom.pose.pose.orientation = Quaternion(
            *quaternion_from_euler(
                0, radians(heading.pitch), radians(heading.heading)
            )
        )
        odom.pose.covariance[0] = pow(bestxyz.p_x_std, 2)
        odom.pose.covariance[7] = pow(bestxyz.p_y_std, 2)
        odom.pose.covariance[14] = pow(bestxyz.p_z_std, 2)
        odom.pose.covariance[28] = pow(heading.ptchstddev, 2)
        odom.pose.covariance[35] = pow(heading.hgdstddev, 2)

        odom.twist.twist.linear.x = bestxyz.v_x
        odom.twist.twist.linear.y = bestxyz.v_y
        odom.twist.twist.linear.z = bestxyz.v_z
        odom.twist.covariance[0] = pow(bestxyz.v_x_std, 2)
        odom.twist.covariance[7] = pow(bestxyz.v_y_std, 2)
        odom.twist.covariance[14] = pow(bestxyz.v_z_std, 2)

        self.publisher.publish(odom)

        if self.publish_tf:
            self.tf_broadcast.sendTransform(
                odom.pose.pose.position,
                odom.pose.pose.orientation,
                odom.header.stamp,
                odom.child_frame_id,
                odom.header.frame_id,
            )
        self.seq += 1
