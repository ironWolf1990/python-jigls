from __future__ import annotations

import logging
from typing import Any, Dict, Optional

from jigls.jeditor.base.socketbase import JBaseSocket
from jigls.jeditor.jdantic import JEdgeModel
from jigls.logger import logger
from jigls.jeditor.utils import UniqueIdentifier

logger = logging.getLogger(__name__)


class JBaseEdge(object):
    def __init__(
        self,
        startSocket=JBaseSocket,
        destnSocket: Optional[JBaseSocket] = None,
        uid: Optional[str] = None,
    ) -> None:
        self._uid: str = UniqueIdentifier() if uid is None else uid
        self._startSocket: JBaseSocket = startSocket
        self._destnSocket: Optional[JBaseSocket] = destnSocket

        self._startSocket.ConnectEdge(self._uid)
        if self._destnSocket is not None:
            self._destnSocket.ConnectEdge(self._uid)

    @property
    def uid(self):
        return self._uid

    @property
    def startSocket(self):
        return self._startSocket

    @property
    def destnSocket(self):
        return self._destnSocket

    @destnSocket.setter
    def destnSocket(self, destnSocket: JBaseSocket) -> None:
        if destnSocket.AtMaxLimit():
            logger.error(f"E:{self._uid} D:{destnSocket.uid} max edge limit reached")
            return None
        self._destnSocket = destnSocket

    def DisconnectFromSockets(self):
        self._startSocket.DisconnectEdge(self._uid)
        if self._destnSocket is not None:
            self._destnSocket.DisconnectEdge(self._uid)

    def ReconnectToSockets(self):
        self._startSocket.ConnectEdge(self._uid)
        if self._destnSocket is not None:
            self._destnSocket.ConnectEdge(self._uid)

    def __repr__(self) -> str:
        return "U:%s S:%s D:%s" % (self.uid, self.startSocket, self.destnSocket)

    def Serialize(self) -> JEdgeModel:
        return JEdgeModel(
            uid=self.uid,
            startSocket=self.startSocket.uid,
            destnSocket=self.destnSocket.uid,
        )

    @classmethod
    def Deserialize(
        cls, uid: str, startSocket: JBaseSocket, destnSocket: JBaseSocket
    ) -> Optional[JBaseEdge]:

        if startSocket.AtMaxLimit():
            logger.error(
                f"E:{uid} S:{startSocket.uid} D:{destnSocket.uid}, start socket at max conection limit"
            )
            return None
        elif destnSocket.AtMaxLimit():
            logger.error(
                f"E:{uid} S:{startSocket.uid} D:{destnSocket.uid}, destn socket at max conection limit"
            )
            return None

        return JBaseEdge(uid=uid, startSocket=startSocket, destnSocket=destnSocket)

    @classmethod
    def NewEdge(cls, startSocket: JBaseSocket) -> Optional[JBaseEdge]:

        if startSocket.AtMaxLimit():
            logger.error("error deserializing edge, start socket at max limit")
            return None

        return JBaseEdge(startSocket=startSocket)
