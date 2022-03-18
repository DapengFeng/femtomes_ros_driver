from io import BytesIO
import time

from femtomes_ros_driver.msg import FemtomesHeader
import genpy
import rospy
from std_msgs.msg import Header


class FemtomesTranslator(object):
    def __init__(
        self,
        name: str,
        data_class: genpy.Message,
    ) -> None:
        self.message = data_class()
        self.publisher = rospy.Publisher(
            "femtomes/" + name, data_class, queue_size=1
        )
        self.seq = 0
        self.frame_id = "femtomes_raw_data"

    def translate(self, buff: bytes, header: FemtomesHeader) -> None:
        std_header = Header()
        std_header.seq = self.seq
        std_header.stamp = rospy.Time(
            header.week * 7 * 24 * 60 * 60 + header.ms / 1000,
            header.ms % 1000 * 1000000,
        )
        std_header.frame_id = self.frame_id
        std_header_buff = BytesIO()
        std_header.serialize(std_header_buff)
        buff = std_header_buff.getvalue() + buff
        self.message.deserialize(buff)
        rospy.loginfo(time.ctime(self.message.header.stamp.to_sec()))
        self.publisher.publish(self.message)
        self.seq += 1
