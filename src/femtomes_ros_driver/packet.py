from io import StringIO
import socket
import threading
from typing import Any
from typing import Callable
from typing import Iterable
from typing import Mapping
from typing import Optional
from typing import Tuple

from femtomes_ros_driver import msg
import rospy

from .mapping import msgs
from .publisher import FemtomesPublisher
from .translator import FemtomesTranslator


class Packet(threading.Thread):
    """Common base class. Provides functionally to recv/send femtomes-formatted
    packets."""

    def __init__(
        self,
        sock: socket.socket,
        group: Any = None,
        target: Optional[Callable[..., Any]] = None,
        name: Optional[str] = None,
        args: Iterable[Any] = ...,
        kwargs: Optional[Mapping[str, Any]] = None,
        *,
        daemon: Optional[bool] = None,
    ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.sock = sock
        self.finish = threading.Event()
        self.translators = {}
        for msg_id in msgs.keys():
            self.translators[msg_id] = FemtomesTranslator(*msgs[msg_id])
        self.publisher = FemtomesPublisher("bestxyz", "heading")

    def recv(
        self,
    ) -> Tuple[
        Optional[msg.FemtomesHeader],
        Optional[StringIO],
        Optional[msg.FemtomesFooter],
    ]:
        """Receive a packet from the socket."""
        header = msg.FemtomesHeader()
        footer = msg.FemtomesFooter()

        try:
            # bytes_before_sync = []
            while True:
                sync = self.sock.recv(1)
                if sync == b"\xaa":
                    # bytes_before_sync = "".join(str(bytes_before_sync))
                    # if len(
                    #     bytes_before_sync
                    # ) > 0 and not bytes_before_sync.startswith("\r\n<OK"):
                    #     rospy.logwarn(
                    #         f"Discarded {len(bytes_before_sync)} bytes "
                    #         "between end of previous message and next sync "
                    #         "byte."
                    #     )
                    #     rospy.logwarn(f"Discarded: {repr(bytes_before_sync)}")
                    break
                # bytes_before_sync.append(sync)

            sync = self.sock.recv(1)
            if sync != b"\x44":
                raise ValueError(
                    f"Bad preamble2 byte, should be 0x44, received "
                    f"0x{ord(sync[0])}"
                )
            sync = self.sock.recv(1)
            if sync != b"\x12":
                raise ValueError(
                    f"Bad preamble3 byte, should be 0x44, received "
                    f"0x{ord(sync[0])}"
                )

            # Four byte offset to account for 3 preamble3 bytes and on header
            # length byte already consumed.
            header_length = ord(self.sock.recv(1)) - 4

        except socket.timeout:
            return None, None, None

        header_buf = self.sock.recv(header_length)
        header.deserialize(header_buf)

        packect_buf = self.sock.recv(header.message_length)
        footer_buf = self.sock.recv(4)
        footer.deserialize(footer_buf)

        return header, packect_buf, footer

    def send(self, message: str) -> None:
        self.sock.send(message.encode())

    def run(self) -> None:
        messages = {}
        while not self.finish.is_set():
            try:
                header, pkt_str, _ = self.recv()
                if header is not None:
                    messages[msgs[header.message_id][0]] = self.translators[
                        header.message_id
                    ].translate(pkt_str, header)

            except ValueError as e:
                # Some problem in the recv() routine.
                rospy.logwarn(str(e))
                continue

            except KeyError:
                if header.message_id not in messages:
                    rospy.logwarn(
                        f"No publisher for message id {header.message_id}"
                    )
