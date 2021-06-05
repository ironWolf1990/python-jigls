from jigls.jcore.ioperation import JOperation
from jigls.jeditor.constants import JCONSTANTS
from jigls.jcore import INode, ISocket


def _iOpNot(a: bool):
    return not a


class iGate2Node(INode):
    def __init__(self, name):
        super().__init__(name, monitor=True)
        self.AddSocket(
            ISocket(
                pNode=self,
                name="A",
                type=JCONSTANTS.SOCKET.TYPE_INPUT,
                dataType=bool,
            )
        )
        self.AddSocket(
            ISocket(
                pNode=self,
                name="A",
                type=JCONSTANTS.SOCKET.TYPE_INPUT,
                dataType=bool,
            )
        )
        self.AddSocket(
            ISocket(
                pNode=self,
                name="B",
                type=JCONSTANTS.SOCKET.TYPE_OUTPUT,
                dataType=bool,
            )
        )


class iNot(INode):
    def __init__(self, name):
        super().__init__(name, monitor=True)
        self.AddSocket(
            ISocket(
                pNode=self,
                name="A",
                type=JCONSTANTS.SOCKET.TYPE_INPUT,
                dataType=bool,
            )
        )
        self.AddSocket(
            ISocket(
                pNode=self,
                name="B",
                type=JCONSTANTS.SOCKET.TYPE_OUTPUT,
                dataType=bool,
            )
        )
        self.AddOperation(
            JOperation(name="Not", inputs=["A"], outputs=["B"], fn=_iOpNot)
        )


# class And(Gate2Node):
#     def __init__(self, name):
#         Gate2Node.__init__(self, name)

#     def Compute(self):
#         self.C.Set(self.A._data and self.B._data)
