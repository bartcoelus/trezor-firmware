# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TxAckPrevTxType import TxAckPrevTxType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckPrevMeta(p.MessageType):
    MESSAGE_WIRE_TYPE = 22

    def __init__(
        self,
        *,
        tx: TxAckPrevTxType,
    ) -> None:
        self.tx = tx

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tx', TxAckPrevTxType, p.FLAG_REQUIRED),
        }
