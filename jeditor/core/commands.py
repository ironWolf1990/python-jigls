from jeditor.core.graphicedge import JGraphicEdge
from jeditor.core.graphicnode import JGraphicNode
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGraphicsScene


class NodeAddCommand(QtWidgets.QUndoCommand):
    def __init__(self, graphicScene: QGraphicsScene, node: JGraphicNode) -> None:
        super().__init__()
        self._graphicScene: QGraphicsScene = graphicScene
        self._node: JGraphicNode = node
        self.setText(f"add node {self._node.nodeId}")

    def undo(self) -> None:
        self._graphicScene.removeItem(self._node)

    def do(self) -> None:
        self._graphicScene.addItem(self._node)


class NodeRemoveCommand(QtWidgets.QUndoCommand):
    def __init__(self, graphicScene: QGraphicsScene, node: JGraphicNode) -> None:
        super().__init__()
        self._graphicScene: QGraphicsScene = graphicScene
        self._node: JGraphicNode = node
        self.setText(f"remove node {self._node.nodeId}")

    def undo(self) -> None:
        self._graphicScene.addItem(self._node)

    def do(self) -> None:
        self._graphicScene.removeItem(self._node)


class NodeMoveCommand(QtWidgets.QUndoCommand):
    ...
    # def __init__(self, graphicScene: QGraphicsScene, node: JGraphicNode) -> None:
    #     super().__init__()
    #     self._graphicScene: QGraphicsScene = graphicScene
    #     self._node: JGraphicNode = node
    #     self.setText(f"delete node {self._node.nodeId}")

    # def undo(self) -> None:
    #     self._graphicScene.addItem(self._node)

    # def redo(self) -> None:
    #     self._graphicScene.removeItem(self._node)


class EdgeAddCommand(QtWidgets.QUndoCommand):
    def __init__(self, graphicScene: QGraphicsScene, edge: JGraphicEdge) -> None:
        super().__init__()
        self._graphicScene: QGraphicsScene = graphicScene
        self._edge: JGraphicEdge = edge
        self.setText(f"add edge {self._edge.edgeId}")

    def undo(self) -> None:
        self._graphicScene.removeItem(self._edge)
        self._edge.DisconnectFromSockets()

    def do(self) -> None:
        self._graphicScene.addItem(self._edge)
        self._edge.ReconnectToSockets()


class EdgeRemoveCommand(QtWidgets.QUndoCommand):
    def __init__(self, graphicScene: QGraphicsScene, edge: JGraphicEdge) -> None:
        super().__init__()
        self._graphicScene: QGraphicsScene = graphicScene
        self._edge: JGraphicEdge = edge
        self.setText(f"delete edge {self._edge.edgeId}")

    def undo(self) -> None:
        self._edge.ReconnectToSockets()
        self._graphicScene.addItem(self._edge)

    def do(self) -> None:
        self._edge.DisconnectFromSockets()
        self._graphicScene.removeItem(self._edge)
