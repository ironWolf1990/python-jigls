from PyQt5 import QtWidgets
from typing import Optional
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QGraphicsSceneMouseEvent,
    QGraphicsTextItem,
    QLabel,
    QScrollArea,
    QStyleOptionGraphicsItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class JNodeContent(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):
        # return
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll)

        for i in range(1, 50):
            object = QLabel("TextLabel")
            vbox.addWidget(object)
