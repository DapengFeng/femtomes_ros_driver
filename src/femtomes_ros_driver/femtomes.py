import socket

import rospy

from .packet import Packet


class Femtomes(object):
    def __init__(self, ip: str, port: str, timeout: float = 100.0) -> None:
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip, self.port))
            rospy.loginfo(
                f"Successfully connected to {self.ip} port at {self.port}"
            )
        except socket.error as e:
            rospy.logfatal(
                f"Couldn't connect to {self.ip} at {self.port}, {str(e)}"
            )
            exit(1)
        self.sock.settimeout(timeout)
        self.packet = Packet(self.sock)

    def capture(self) -> None:
        receiver_config = rospy.get_param("~configuration", None)

        if receiver_config is not None:
            logger = receiver_config.get("log_request", [])
            rospy.loginfo(
                f"Enabling {len(logger)} log outputs from Femtomes system."
            )
            for log in logger:
                self.packet.send(
                    "log " + log + " ontime " + str(logger[log]) + "\r\n"
                )

            commands = receiver_config.get("command", [])
            rospy.loginfo(
                f"Sending {len(commands)} user-specified initialization "
                "commands to Femtomes Receiver."
            )
            for cmd in commands:
                self.packet.send(cmd + " " + str(commands[cmd]) + "\r\n")

        self.packet.start()
        rospy.loginfo(f"{self.ip}:{self.port} started.")

        def shutdown() -> None:
            self.packet.finish.set()
            self.packet.join()
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            rospy.loginfo(f"{self.ip}:{self.port} closed.")

        rospy.on_shutdown(shutdown)
