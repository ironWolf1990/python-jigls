from jigls.jeditor.constants import JCONSTANTS
import uuid

from PyQt5 import QtCore


def UniqueIdentifier() -> str:
    return uuid.uuid4().hex
