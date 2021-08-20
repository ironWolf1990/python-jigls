from jigls.jeditor.widgets.graphicsnodecontent import JGraphicNodeContent
from typing import Optional
from PyQt5.QtCore import QPointF

from PyQt5.QtWidgets import QGraphicsItem
from jigls.jeditor.jdantic import JGraphNodeModel
from jigls.jeditor.base.nodebase import JBaseNode
from jigls.jeditor.ui.graphicnode import JGraphicsNode


class A(JGraphicsNode):

    __TYPE__: str = "A"

    def __init__(self, baseNode: JBaseNode, parent: Optional[QGraphicsItem] = None) -> None:
        super().__init__(baseNode, parent=parent)

        self.AddInputSocket("in1", True)
        self.AddOutputSocket("out1", True)

        self.dataContent.AddComboBox(label="Group", options=[str(x + 1) for x in range(10)])
        self.dataContent.AddComboBox(
            label="Element Type", options=["Dropdown", "Text", "Checkbox", "RadioButton", "RadioCheckbox"]
        )
        self.dataContent.AddTextEdit(label="Description", placeholder="dummy description ...")
        self.dataContent.AddSectionTree(label="XPath", sectionName="XPath")
        self.dataContent.AddSectionTree(label="Value", sectionName="Value")
        self.dataContent.AddLineEdit(label="Action", placeholder="action ...")

        self.baseNode.exec = False

        self.contentWidget = JGraphicNodeContent()

        self.contentWidget.displayText.setText(
            self.dataContent.GetData("Description").toPlainText()  # type:ignore
        )
        self.dataContent.GetData("Description").textChanged.connect(self._UpdateContent)  # type:ignore

        self.baseNode.exec = False

    def _UpdateContent(self):
        self.contentWidget.displayText.setText(  # type:ignore
            self.dataContent.GetData("Description").toPlainText()  # type:ignore
        )


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