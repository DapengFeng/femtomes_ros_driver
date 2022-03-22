import socket

import rospy

from .packet import Packet


class Femtomes(object):
    def __init__(self, ip, port, timeout = 100.0):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip, self.port))
            rospy.loginfo(
                "Successfully connected to %s port at %d" % (self.ip, self.port)
            )
        except socket.error as e:
            rospy.logfatal(
                "Couldn't connect to %s at %d, %s" %(self.ip, self.port, str(e))
            )
            exit(1)
        self.sock.settimeout(timeout)
        self.packet = Packet(self.sock)

    def capture(self):
        receiver_config = rospy.get_param("~configuration", None)

        if receiver_config is not None:
            logger = receiver_config.get("log_request", [])
            rospy.loginfo(
                "Enabling %d log outputs from Femtomes system." % len(logger)
            )
            for log in logger:
                self.packet.send(
                    "log " + log + " ontime " + str(logger[log]) + "\r\n"
                )

            commands = receiver_config.get("command", [])
            rospy.loginfo(
                "Sending %d user-specified initialization commands to Femtomes Receiver." % len(commands)
            )
            for cmd in commands:
                self.packet.send(cmd + " " + str(commands[cmd]) + "\r\n")

        self.packet.start()
        rospy.loginfo("%s:%d started." % (self.ip, self.port))

        def shutdown():
            self.packet.finish.set()
            self.packet.join()
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            rospy.loginfo("%s:%d closed." % (self.ip, self.port))

        rospy.on_shutdown(shutdown)
