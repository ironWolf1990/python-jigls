import typing
from PyQt5 import QtWidgets
from typing import Optional
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QGraphicsProxyWidget,
    QGraphicsSceneMouseEvent,
    QGraphicsTextItem,
    QLabel,
    QLineEdit,
    QScrollArea,
    QStyleOptionGraphicsItem,
    QTextEdit,
    QPlainTextEdit,
    QVBoxLayout,
    QWidget,
)


class JNodeNameText(QLineEdit):
    def __init__(self, parent=None) -> None:
        return super().__init__(parent=parent)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        return

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        return


class JProxyWidget(QGraphicsProxyWidget):
    def __init__(self, parent: typing.Optional[QGraphicsItem]) -> None:
        super().__init__(parent=parent)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        return super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        return super().mouseDoubleClickEvent(event)


class JNodeNameWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):

        object = JNodeNameText(self)
        object.event
        object.setText("12345678910111213")
        object.setAutoFillBackground(True)
        object.setReadOnly(True)

        # scroll = QScrollArea()
        # scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # scroll.setWidgetResizable(False)
        # scroll.setWidget(object)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(object)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        return