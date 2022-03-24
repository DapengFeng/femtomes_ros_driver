from io import BytesIO

import rospy
from std_msgs.msg import Header


class FemtomesTranslator(object):
    def __init__(
        self,
        name,
        data_class,
    ):
        self.message = data_class()
        self.publisher = rospy.Publisher(
            "femtomes/" + name, data_class, queue_size=1
        )
        self.seq = 0
        self.frame_id = "femtomes_raw_data"

    def translate(self, buff, header):
        std_header = Header()
        std_header.seq = self.seq
        if header.week != 0:
            std_header.stamp = rospy.Time(
                header.week * 7 * 24 * 60 * 60
                + int(header.ms / 1000)
                + 315964800,
                header.ms % 1000 * 1000000,
            )
        else:
            std_header.stamp = rospy.Time.now()
        std_header.frame_id = self.frame_id
        std_header_buff = BytesIO()
        std_header.serialize(std_header_buff)
        buff = std_header_buff.getvalue() + buff
        self.message.deserialize(buff)
        # rospy.loginfo(time.ctime(self.message.header.stamp.to_sec()))
        self.publisher.publish(self.message)
        self.seq += 1
