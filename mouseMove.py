try:
    from PySide import QtCore, QtGui
except ImportError:
    from PyQt4 import QtCore, QtGui

class Widget(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        scene = QtGui.QGraphicsScene(self)
        item = QtGui.QGraphicsRectItem(0, 0, 100, 100)
        item.setAcceptHoverEvents(True)
        scene.addItem(item)
        self.setScene(scene)

    def mouseMoveEvent(self, evt):
        print "mouse move",  evt.pos()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
