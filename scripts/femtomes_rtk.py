#! /usr/bin/env python
import femtomes_ros_driver.femtomes as femtomes
import rospy


def main():
    rospy.init_node("femtomes_rtk")
    ip = rospy.get_param("~ip")
    port = rospy.get_param("~port")
    rtk = femtomes.Femtomes(ip, port)
    rtk.capture()
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException as e:
        print(e)
