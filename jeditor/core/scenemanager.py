from jeditor.core.edgemanager import JEdgeDragging, JEdgeRerouting
from jeditor.core.commands import (
    EdgeAddCommand,
    EdgeRemoveCommand,
    EdgeRerouteCommand,
    NodeRemoveCommand,
)
import json
import logging
from typing import Dict, List, Optional, Tuple
import typing

from jeditor.logger import logger
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QUndoStack
from .constants import JCONSTANTS
from .graphicedge import JGraphicEdge
from .graphicnode import JGraphicNode
from .graphicscene import JGraphicScene
from .graphicsocket import JGraphicSocket
from .nodefactory import JNodeFactory

logger = logging.getLogger(__name__)


class JSceneManager(QtCore.QObject):
    def __init__(self) -> None:
        super().__init__(parent=None)

        self._graphicsScene = JGraphicScene()

        self._nodeFactory = JNodeFactory()
        self._undoStack = QUndoStack(self._graphicsScene)
        self._edgeDragging = JEdgeDragging(self._graphicsScene)
        self._edgeReroute = JEdgeRerouting(self._graphicsScene)

        self._graphicsScene.SetWidthHeight(
            JCONSTANTS.GRSCENE.WIDTH, JCONSTANTS.GRSCENE.HEIGHT
        )

        self._debug()

    @property
    def graphicsScene(self) -> JGraphicScene:
        return self._graphicsScene

    @property
    def undoStack(self) -> QUndoStack:
        return self._undoStack

    def _debug(self):
        node1 = self._nodeFactory.CreateNode(None, False, False)
        node2 = self._nodeFactory.CreateNode(None, True, True)
        node3 = self._nodeFactory.CreateNode(None, True, False)
        # node4 = JGraphicNode(inSockets=1, outSockets=1, nodeContent=JNodeContent())

        node1.setPos(QPointF(-350, -250))
        node2.setPos(QPointF(-75, 0))
        node3.setPos(QPointF(0, 0))

        self.graphicsScene.addItem(node1)
        self.graphicsScene.addItem(node2)
        self.graphicsScene.addItem(node3)

    def Serialize(self) -> Dict:
        logger.info("serializing")
        node: List[Dict] = []
        edge: List[Dict] = []
        for item in self._graphicsScene.items():
            if isinstance(item, JGraphicNode):
                node.append(item.Serialize())
            if isinstance(item, JGraphicEdge):
                edge.append(item.Serialize())
        return {"nodes": node, "edges": edge}

    def Deserialize(self, data: Dict):
        logger.info("deserializing")

        self._graphicsScene.clear()
        self._undoStack.clear()

        for node in data["nodes"]:
            instanceNode = JGraphicNode.Deserialize(node)
            self._graphicsScene.addItem(instanceNode)

        for edge in data["edges"]:
            edgeId = edge["edgeId"]
            sourceSocketId = edge["sourceSocketId"]
            desitnationSocketId = edge["desitnationSocketId"]

            sourceSocket: Optional[JGraphicSocket] = None
            destinationSocket: Optional[JGraphicSocket] = None

            for socket in list(
                filter(
                    lambda socket_: isinstance(socket_, JGraphicSocket),
                    self._graphicsScene.items(),
                )
            ):
                assert isinstance(socket, JGraphicSocket)
                if socket.socketId == sourceSocketId:
                    sourceSocket = socket
                elif socket.socketId == desitnationSocketId:
                    destinationSocket = socket

            assert sourceSocket, logger.error("source socket not found")
            assert destinationSocket, logger.error("destination socket not found")

            instanceEdge = JGraphicEdge.Deserialize(
                edgeId, sourceSocket, destinationSocket
            )

            self._graphicsScene.addItem(instanceEdge)

    def SaveToFile(self):
        logger.debug("saving to file")
        with open("graph.json", "w") as file:
            json.dump(obj=self.Serialize(), fp=file)

    def LoadFromFile(self) -> Dict:
        logger.debug("loading from file")
        with open("graph.json", "r") as file:
            data = json.load(file)
            return data

    def StartEdgeDrag(self, item: QtWidgets.QGraphicsItem) -> bool:
        assert isinstance(item, JGraphicSocket)
        return self._edgeDragging.StartDrag(item)

    def EndEdgeDrag(self, item: QtWidgets.QGraphicsItem) -> bool:
        ret = self._edgeDragging.EndDrag(item)
        if ret:
            edge = self._edgeDragging._tempEdge
            assert edge is not None

            logger.debug(f"add new edge {edge.edgeId}")

            self.undoStack.beginMacro("add edge")
            self.undoStack.push(
                EdgeAddCommand(graphicScene=self.graphicsScene, edge=edge)
            )
            self.undoStack.endMacro()

            self._edgeDragging.Reset()

        return ret

    def StartEdgeReRoute(self, cursorPos: QtCore.QPointF) -> bool:
        if len(self._graphicsScene.selectedItems()) == 0:
            logger.warning("no edge selected for rerouting")
            return False
        elif len(self._graphicsScene.selectedItems()) > 1:
            logger.warning("multiple items selected for rerouting. select 1 edge")
            return False

        assert self._graphicsScene.selectedItems(), logger.error(
            f"initial edge rerouting condition check failed"
        )

        item = self._graphicsScene.selectedItems()[0]

        if not isinstance(item, JGraphicEdge):
            logger.warning("none edge type selected for rerouting")
            return False
        elif isinstance(item, JGraphicEdge):
            self._edgeReroute.StartRerouting(item, cursorPos)
            return True

        logger.error("edge rerouting failed")
        return False

    def EndEdgeReRoute(self, item: QtWidgets.QGraphicsItem) -> bool:
        ret = self._edgeReroute.EndRerouting(item)
        if ret:
            edge = self._edgeReroute._tempEdge
            nDestinationSocket = self._edgeReroute._nDestinationSocket

            assert edge is not None
            assert nDestinationSocket is not None

            logger.debug(f"rerouting edge {edge.edgeId}")
            self.undoStack.beginMacro("rerouting edge")
            self.undoStack.push(
                EdgeRerouteCommand(
                    graphicScene=self.graphicsScene,
                    edge=edge,
                    nDestinationSocket=nDestinationSocket,
                )
            )
            self.undoStack.endMacro()
            self._edgeReroute.Reset()
        return ret

    def RemoveFromScene(self):
        if not self._graphicsScene.selectedItems():
            logger.debug("no items to delete")
            return

        edgeIdRemove: typing.Set[str] = set()
        nodeIdRemove: typing.Set[str] = set()

        for item in self._graphicsScene.selectedItems():
            if isinstance(item, JGraphicNode):
                nodeIdRemove.add(item.nodeId)
                for socket in item.socketManager.socketList:
                    edgeIdRemove |= set(socket.edgeList)
            elif isinstance(item, JGraphicEdge):
                edgeIdRemove.add(item.edgeId)
            else:
                logger.debug(f"unknown item selected in delete type {type(item)}")

        logger.debug(f"nodes marked for removal {nodeIdRemove}")
        logger.debug(f"edges marked for removal {edgeIdRemove}")

        self.undoStack.beginMacro("remove item")
        # * first always remove edges, easier to implement undo stack!
        self.RemoveEdgesFromScene(edgeIdRemove)
        self.RemoveNodesFromScene(nodeIdRemove)
        self.undoStack.endMacro()

    def RemoveNodesFromScene(self, nodes: typing.Set[str]):
        for node in nodes:
            self.RemoveNodeFromScene(node)

    def RemoveEdgesFromScene(self, edges: typing.Set[str]):
        for edge in edges:
            self.RemoveEdgeFromScene(edge)

    def RemoveNodeFromScene(self, nodeId: str):
        node_ = list(
            filter(
                lambda node: isinstance(node, JGraphicNode) and node.nodeId == nodeId,
                self._graphicsScene.items(),
            )
        )
        assert len(node_) == 1, logger.error(
            f"error fetching node {nodeId} for removal"
        )

        node__ = node_[0]
        assert isinstance(node__, JGraphicNode)

        logger.debug(f"remove node {nodeId}")
        self.undoStack.beginMacro("remove node")
        self.undoStack.push(
            NodeRemoveCommand(graphicScene=self.graphicsScene, node=node__)
        )
        self.undoStack.endMacro()

    def RemoveEdgeFromScene(self, edgeId: str):
        edge_ = list(
            filter(
                lambda edge: isinstance(edge, JGraphicEdge) and edge.edgeId == edgeId,
                self._graphicsScene.items(),
            )
        )
        assert len(edge_) == 1, logger.error(
            f"error fetching node {edgeId} for removal"
        )

        edge__ = edge_[0]
        assert isinstance(edge__, JGraphicEdge)

        logger.debug(f"remove edge {edgeId}")
        self.undoStack.beginMacro("remove edge")
        self.undoStack.push(
            EdgeRemoveCommand(graphicScene=self.graphicsScene, edge=edge__)
        )
        self.undoStack.endMacro()

    def DebugSceneInformation(self):
        print(f"\n{30*'='}\n{10*'-'} SCENE NODES")
        for item in self._graphicsScene.items():
            if isinstance(item, (JGraphicNode)):
                print(item.nodeId)
        print(f"{10*'-'} SCENE EDGES")
        for item in self._graphicsScene.items():
            if isinstance(item, (JGraphicEdge)):
                print(item.edgeId)
        print(f"{10*'-'} SCENE CONNECTIONS")
        ...
        print(f"{30*'='}\n")