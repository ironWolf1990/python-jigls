import logging
from typing import Dict, List, Optional, Tuple, Union
import json
from jigls.jeditor.stylesheet import STYLE_TREE
from jigls.jeditor.widgets.custom import (
    DelegateTreeOperations,
    JQComboBox,
    JQLabel,
    JQLineEdit,
    JQTextEdit,
    PropertiesSection,
    PropertyTree,
)
from jigls.logger import logger
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QValidator
from PyQt5.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QScrollArea,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

logger = logging.getLogger(__name__)


from typing import Optional


class JGraphicNodeContent(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)

        self.displayText = JQTextEdit("this is show content")

        self.initUI()

    def initUI(self):
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(2, 2, 2, 2)
        self.layout().addWidget(self.displayText)