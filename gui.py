import sys

from PyQt5.QtWidgets import QApplication

from jigls.jeditor.editorwindow import JEditorWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wnd = JEditorWindow()
    wnd.show()

    try:
        app.exec_()
    except Exception as e:
        print(e)
