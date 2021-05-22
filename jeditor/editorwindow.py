from jeditor.editormenu import JMenuBar
from jeditor.core.constants import JCONSTANTS
from jeditor.core.editorwidget import JEditorWidget
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class JEditorWindow(QMainWindow):
    def __init__(
        self,
        parent: typing.Optional[QtWidgets.QWidget] = None,
    ) -> None:
        super().__init__(parent=parent)

        self._editorWidget = JEditorWidget(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)
        # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

        self.setCentralWidget(self._editorWidget)

        menuBar = JMenuBar(self._editorWidget)
        self.setMenuBar(menuBar)

        self.statusBar().showMessage("this is message")

        self.setGeometry(200, 200, JCONSTANTS.EDITOR.WIDTH, JCONSTANTS.EDITOR.HEIGHT)
        self.setWindowTitle(JCONSTANTS.EDITOR.TITLE)
