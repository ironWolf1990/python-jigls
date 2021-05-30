from PyQt5 import QtCore, QtGui


class JGraphicEdgeDirect:
    @staticmethod
    def GetPath(
        sourcePos: QtCore.QPointF, destinationPos: QtCore.QPointF
    ) -> QtGui.QPainterPath:
        s = sourcePos
        d = destinationPos

        path = QtGui.QPainterPath(s)
        path.lineTo(d)
        return path


class JGraphicEdgeSquare:
    @staticmethod
    def GetPath(
        sourcePos: QtCore.QPointF, destinationPos: QtCore.QPointF, hndWeight=0.5
    ) -> QtGui.QPainterPath:
        s = sourcePos
        d = destinationPos

        mid_x = s.x() + ((d.x() - s.x()) * hndWeight)

        path = QtGui.QPainterPath(QtCore.QPointF(s.x(), s.y()))
        path.lineTo(mid_x, s.y())
        path.lineTo(mid_x, d.y())
        path.lineTo(d.x(), d.y())
        return path


class JGraphicEdgeBezier:
    @staticmethod
    def GetPath(
        sourcePos: QtCore.QPointF, destinationPos: QtCore.QPointF
    ) -> QtGui.QPainterPath:
        s = sourcePos
        d = destinationPos

        dist = abs(s.x() - d.x()) // 2

        path = QtGui.QPainterPath(QtCore.QPointF(s.x(), s.y()))
        path.cubicTo(s.x() + dist, s.y(), d.x() - dist, d.y(), d.x(), d.y())
        return path
