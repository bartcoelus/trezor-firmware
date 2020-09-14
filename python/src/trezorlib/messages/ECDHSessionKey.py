# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class ECDHSessionKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 62

    def __init__(
        self,
        *,
        session_key: bytes = None,
    ) -> None:
        self.session_key = session_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('session_key', p.BytesType, None),
        }
