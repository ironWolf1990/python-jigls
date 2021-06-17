from argparse import Namespace, ArgumentParser
from jigls.profiler import Profile

import sys
from PyQt5.QtWidgets import QApplication
from jigls.jeditor.editorwindow import JEditorWindow


def Run():

    app = QApplication(sys.argv)
    wnd = JEditorWindow()

    try:
        wnd.show()
        app.exec_()
    except Exception as e:
        print(e)


def main(args=Namespace):

    if args.profile:
        Profile()(Run)
    else:
        Run()


if __name__ == "__main__":

    parser = ArgumentParser(description="command line arguments")

    parser.add_argument("--profile", action="store_false")

    main(parser.parse_args())
