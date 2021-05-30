import sys
from typing import Optional, Union
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QLayout,
    QLineEdit,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QApplication,
)


class Xpath(QWidget):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Optional[Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType]] = None,
    ) -> None:
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):

        layout_ = QVBoxLayout()

        self.xpathOperation = QHBoxLayout()
        self.addButton = QPushButton("add xpath")
        self.removeButton = QPushButton("remove xpath")

        self.addButton.clicked.connect(self.add)
        self.removeButton.clicked.connect(self.remove)

        self.xpathOperation.addWidget(self.addButton)
        self.xpathOperation.addWidget(self.removeButton)

        layout_.addLayout(self.xpathOperation)
        self.setLayout(layout_)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.show()

    def add(self):
        Button1 = QLineEdit(str(self.layout().count()))
        self.layout().addWidget(Button1)

    def remove(self):
        if self.layout().count() > 1:
            self.layout().itemAt(self.layout().count() - 1).widget().deleteLater()
        else:
            print("nope")


class Value(QWidget):
    def __init__(
        self,
        parent: Optional[QWidget] = None,
        flags: Optional[Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType]] = None,
    ) -> None:
        super().__init__(parent=parent)

        self.initUI()

    def initUI(self):

        layout_ = QVBoxLayout()

        self.xpathOperation = QHBoxLayout()
        self.addButton = QPushButton("add value")
        self.removeButton = QPushButton("remove value")

        self.addButton.clicked.connect(self.add)
        self.removeButton.clicked.connect(self.remove)

        self.xpathOperation.addWidget(self.addButton)
        self.xpathOperation.addWidget(self.removeButton)

        layout_.addLayout(self.xpathOperation)
        self.setLayout(layout_)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.show()

    def add(self):
        Button1 = QLineEdit(str(self.layout().count()))
        self.layout().addWidget(Button1)

    def remove(self):
        if self.layout().count() > 1:
            self.layout().itemAt(self.layout().count() - 1).widget().deleteLater()
        else:
            print("nope")


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setLayout(QVBoxLayout())

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.horizontalScrollBar().setEnabled(False)
        self.scrollArea.setSizePolicy(
            QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        )
        self.layout().addWidget(self.scrollArea)

        self.scrollArea.setWidget(QWidget())
        self.scrollArea.widget().setLayout(QVBoxLayout())
        self.scrollArea.widget().layout().setAlignment(QtCore.Qt.AlignTop)

        self.scrollArea.widget().layout().addWidget(Xpath(self))
        self.scrollArea.widget().layout().addWidget(Value(self))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())