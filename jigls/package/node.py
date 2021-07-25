from typing import Optional
from PyQt5.QtCore import QPointF

from PyQt5.QtWidgets import QGraphicsItem
from jigls.jeditor.jdantic import JGrNodeModel
from jigls.jeditor.base.nodebase import JBaseNode
from jigls.jeditor.ui.graphicnode import JGraphicsNode


class A(JGraphicsNode):

    __TYPE__: str = "A"

    def __init__(self, baseNode: JBaseNode, parent: Optional[QGraphicsItem] = None) -> None:
        super().__init__(baseNode, parent=parent)

        self.AddInputSocket("in1", True)
        self.AddOutputSocket("out1", True)

        self.dataContent.AddComboBox(label="1", options=[str(x + 1) for x in range(10)])
        self.dataContent.AddComboBox(label="2", options=["Dropdown", "Text"])
        self.dataContent.AddTextEdit(label="3", placeholder="dummy description ...")
        self.dataContent.AddSectionTree(label="4", sectionName="Data")
        self.dataContent.AddSectionTree(label="5", sectionName="Value")
        self.dataContent.AddLineEdit(label="6", placeholder="placeholder ...")

        self.baseNode.exec = False


class B(JGraphicsNode):

    __TYPE__: str = "B"

    def __init__(self, baseNode: JBaseNode, parent: Optional[QGraphicsItem] = None) -> None:
        super().__init__(baseNode, parent=parent)

        self.AddInputSocket("in1", True)
        self.AddOutputSocket("out1", True)

        self.dataContent.AddComboBox(label="A1", options=["!", "?", "FCUK"])
        self.dataContent.AddLineEdit(label="Z", placeholder="placehold ...")
        self.dataContent.AddLineEdit(label="P", placeholder="Punisher ...")

        self.baseNode.exec = False