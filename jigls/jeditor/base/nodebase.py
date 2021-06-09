from jigls.jcore.ibase import INode, ISocket
from jigls.jeditor.jdantic import JNodeModel
from jigls.jeditor.constants import JCONSTANTS
from jigls.jeditor.base.socketbase import JBaseSocket
import logging
from typing import Dict, List, Optional, OrderedDict, Set

from jigls.jeditor.utils import UniqueIdentifier
from jigls.logger import logger

logger = logging.getLogger(__name__)

from operator import itemgetter, attrgetter


class JBaseNode(INode):
    def __init__(self, name: str, uid: Optional[str] = None) -> None:
        super().__init__(name, uid=uid)

    @property
    def inSocketList(self) -> List[JBaseSocket]:
        return list(  # type:ignore
            filter(
                lambda socket: socket.Type == JCONSTANTS.SOCKET.TYPE_INPUT,
                self.socketList,
            )
        )

    @property
    def outSocketList(self) -> List[JBaseSocket]:
        return list(  # type:ignore
            filter(
                lambda socket: socket.Type == JCONSTANTS.SOCKET.TYPE_OUTPUT,
                self._socketList,
            )
        )

    def AddInputSocket(self, name: str, multiConnection: bool = True):
        self.AddSocket(
            JBaseSocket(
                name=name, pNode=self, type=JCONSTANTS.SOCKET.TYPE_INPUT, multiConnect=multiConnection
            )
        )

    def AddOutputSocket(self, name: str, multiConnection: bool = True):
        self.AddSocket(
            JBaseSocket(
                name=name, pNode=self, type=JCONSTANTS.SOCKET.TYPE_OUTPUT, multiConnect=multiConnection
            )
        )

    def __repr__(self) -> str:
        return super().__repr__()

    def Serialize(self):
        pass
        # return JNodeModel(
        #     name=self.name,
        #     uid=self.uid,
        #     socketList=[socket.Serialize() for socket in self.socketList],
        # )

    @classmethod
    def Deserialize(cls, nodeModel: JNodeModel):
        pass

        # baseNode = JBaseNode(name=nodeModel.name, uid=nodeModel.uid.hex)

        # for socket in sorted(
        #     list(
        #         filter(
        #             lambda socket: socket.type == JCONSTANTS.SOCKET.TYPE_INPUT,
        #             nodeModel.socketList,
        #         )
        #     ),
        #     key=attrgetter("index"),
        # ):
        #     baseNode._socketList.add(
        #         JBaseSocket(
        #             name=socket.name,
        #             uid=socket.uid.hex,
        #             nodeID=socket.nodId.hex,
        #             index=socket.index,
        #             type=socket.type,
        #             multiConnection=socket.multiConnection,
        #         )
        #     )

        # for socket in sorted(
        #     list(
        #         filter(
        #             lambda socket: socket.type == JCONSTANTS.SOCKET.TYPE_OUTPUT,
        #             nodeModel.socketList,
        #         )
        #     ),
        #     key=attrgetter("index"),
        # ):
        #     baseNode._socketList.add(
        #         JBaseSocket(
        #             name=socket.name,
        #             uid=socket.uid.hex,
        #             nodeID=socket.nodId.hex,
        #             index=socket.index,
        #             type=socket.type,
        #             multiConnection=socket.multiConnection,
        #         )
        #     )

        # return baseNode
