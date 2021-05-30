from jigls.base.nodebase import JBaseNode
from typing import Optional
from jigls.constants import JCONSTANTS
from jigls.ui.graphicnode import JGraphicNode
import uuid


class JNodeFactory:
    def __init__(self) -> None:
        pass

    def RegisterNode(self):
        pass

    def CreateNode(self, inputMulti, outputMulti, inputs=1, output=1, *args, **kwargs):

        base = JBaseNode("base node")
        for _ in range(inputs):
            base.AddInputSocket(
                name="in1",
                multiConnection=inputMulti,
            )
        for _ in range(output):
            base.AddOutputSocket(
                name="out1",
                multiConnection=outputMulti,
            )
        node = JGraphicNode(base)

        return node
