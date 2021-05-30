from configparser import Error
from jigls.jdantic import JSocketModel
import logging
from typing import Any, Dict, List, Optional, OrderedDict, Set, Union

from jigls.utils import UniqueIdentifier
from jigls.logger import logger

logger = logging.getLogger(__name__)


class JBaseSocket(object):
    def __init__(
        self,
        name: str,
        index: int,
        nodeID: str,
        type: int,
        dataType=object,
        multiConnection: bool = True,
        uid: Optional[str] = None,
    ):

        self._name: str = name
        self._index: int = index
        self._nodeId: str = nodeID
        self._type: int = type
        self._dataType: object = dataType
        self._multiConnection: bool = multiConnection
        self._uid: str = UniqueIdentifier() if uid is None else uid

        self._data = dataType()
        self._edgeList: Set[str] = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index: int) -> None:
        self._index = index

    @property
    def nodeId(self):
        return self._nodeId

    @nodeId.setter
    def nodeId(self, value: str) -> None:
        self._nodeId = value

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value: str) -> None:
        self._uid = value

    @property
    def type(self):
        return self._type

    @property
    def multiConnection(self):
        return self._multiConnection

    @property
    def dataType(self):
        return self._dataType

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Any) -> None:
        if isinstance(value, self._dataType):  # type:ignore
            self._data = value
        else:
            logger.error(f"N:{self._nodeId} S:{self._uid} V:{value} type missmatch")
            raise TypeError(f"N:{self._nodeId} S:{self._uid} V:{value} type missmatch")

    @property
    def edgeList(self) -> List[str]:
        return list(self._edgeList)

    def ConnectEdge(self, edge: str) -> None:
        assert edge is not None
        if self.AtMaxLimit():
            logger.error(
                f"N:{self._nodeId} S:{self._uid} E:{edge} max edge limit reached"
            )
            logger.debug("error here")
        else:
            self._edgeList.add(edge)

    def DisconnectEdge(self, edge: str):
        self._edgeList.discard(edge)

    def EdgeCount(self) -> int:
        return len(self._edgeList)

    def HasEdge(self, edge: str) -> bool:
        assert edge is not None
        return True if edge in self._edgeList else False

    def AtMaxLimit(self) -> bool:
        if self._multiConnection:
            return False
        # * can add one edge to single connection type
        elif not self._multiConnection and len(self._edgeList) == 0:
            return False
        else:
            return True

    def __repr__(self) -> str:
        return "nm:%s uid:%s pUid:%s idx:%s mC:%s cn:%s" % (
            self.name,
            self.uid,
            self.nodeId,
            self.index,
            self.multiConnection,
            len(self.edgeList),
        )

    def Serialize(self) -> JSocketModel:
        return JSocketModel(
            name=self.name,
            uid=self.uid,
            nodId=self.nodeId,
            index=self.index,
            type=self.type,
            multiConnection=self.multiConnection,
        )

    @classmethod
    def Deserialize(
        cls,
        name: str,
        uid: str,
        nodeId: str,
        index: int,
        type: int,
        multiConnection: bool,
    ):
        return JBaseSocket(
            name=name,
            uid=uid,
            index=index,
            nodeID=nodeId,
            type=type,
            multiConnection=multiConnection,
        )
