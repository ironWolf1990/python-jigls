from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import pickle

iconroot = QFileInfo(__file__).absolutePath()
ORGANIZATION_NAME = "Circularcolumn App"
ORGANIZATION_DOMAIN = "Circular shape"
APPLICATION_NAME = "QSettings program"
SETTINGS_TRAY = "settings/tray"


class UCircularShape(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Frequently used shape")
        self.setWindowIcon(QIcon(iconroot + "/images/circularcolumnnorebar.png"))
        # self.setStyleSheet("background-color:#f2f2f2")

        self.addbutton = QPushButton("Add")
        self.addbutton.clicked.connect(self.add)
        self.deletebutton = QPushButton("Delete")
        self.deletebutton.clicked.connect(self.delete)

        self.okbutton = QPushButton("Ok")
        # self.okbutton.clicked.connect(self.hidethiswindow)
        self.okbutton.clicked.connect(self.savesetting)

        self.cancelbutton = QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.loadsetting)
        # self.cancelbutton.clicked.connect(self.close)

        self.addimage()
        self.qlabeltodefinesection()
        self.Treewidget_()

        self.sectionnamecircular = QLabel("Section name: ")
        self.sectionnamecircularindata = QLineEdit("Define en name to section")
        self.sectionnamecircularindata.setObjectName("sectionnamecircularindata")
        self.sectionnamecircular.setBuddy(self.sectionnamecircularindata)
        self.sectionnamecircular.setFocus()
        self.grid_sectionname = QHBoxLayout()
        self.grid_sectionname.addWidget(self.sectionnamecircular)
        self.grid_sectionname.addWidget(self.sectionnamecircularindata)

        self.boxlayout = QGridLayout()
        self.boxlayout.addLayout(self.grid_sectionname, 0, 0, 1, 2)
        self.boxlayout.addWidget(self.treewidget_, 1, 0, 5, 2)
        self.boxlayout.addWidget(self.addbutton, 2, 2)
        self.boxlayout.addWidget(self.deletebutton, 3, 2)
        self.boxlayout.addWidget(self.imagelabel, 6, 0)
        self.boxlayout.addLayout(self.qlabelhboxgrid, 6, 1)
        self.boxlayout.addWidget(self.okbutton, 8, 1)
        self.boxlayout.addWidget(self.cancelbutton, 8, 2)
        self.setLayout(self.boxlayout)
        try:
            self.loadsetting()
        except (ValueError, TypeError):
            pass

    def Treewidget_(self):
        self.treewidget_ = QTreeWidget(self)
        self.treewidget_.setColumnCount(1)
        self.treewidget_.setColumnWidth(1, 20)
        self.treewidget_.setHeaderItem(QTreeWidgetItem(["Standard Section Library"]))
        # self.treewidget.addTopLevelItem(QTreeWidgetItem(['Standard Sectiontype']))
        self.treewidget_.setRootIsDecorated(True)

        self.firstparentitem = QTreeWidgetItem(self.treewidget_)
        self.firstparentitem.setText(0, "Circular shapes")
        self.firstparentitem.setIcon(
            0, QIcon(iconroot + "/images/circularcolumnnorebar.png")
        )

        standardsectionlist = [
            "D100",
            "D150",
            "D200",
            "D250",
            "D300",
            "D350",
            "D400",
            "D450",
            "D500",
            "D550",
            "D600",
            "D650",
            "D700",
            "D750",
            "D800",
            "D850",
            "D900",
            "D950",
            "D1000",
        ]

        for i in standardsectionlist:
            self.firstparentitem.addChild(QTreeWidgetItem(["%s" % i]))

        self.secondparentitem = QTreeWidgetItem(self.treewidget_)
        self.secondparentitem.setText(0, "Customized")
        self.secondparentitem.setIcon(
            0, QIcon(iconroot + "/images/circularcolumnnorebar.png")
        )
        self.secondchilditem = QTreeWidgetItem(["D235"])
        self.secondparentitem.insertChild(0, self.secondchilditem)
        self.secondchilditem.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicator)
        self.treewidget_.move(15, 15)
        self.treewidget_.setGeometry(15, 15, 200, 600)
        self.treewidget_.setAlternatingRowColors(True)
        self.treewidget_.expandItem(self.firstparentitem)
        self.show()

        print(self.treewidget_.headerItem().text(0))
        print(self.treewidget_.columnCount())
        print(self.treewidget_.currentColumn())

        print(self.treewidget_.indexFromItem(self.firstparentitem).row())
        print(self.firstparentitem.childCount())
        print(self.firstparentitem.child(1).text(0))
        print(self.firstparentitem.text(0))
        print(self.treewidget_.headerItem().text(0))
        print(self.treewidget_.topLevelItem(0).text(0))
        print(self.firstparentitem.isSelected())
        print(self.treewidget_.selectedItems())
        print(self.secondchilditem.text(1))

        branchstyle = """QTreeWidget {border:none;} 

        QTreeView::branch:has-siblings:!adjoins-item {
            border-image: url(images/vline.png) 0;}

        QTreeView::branch:has-siblings:adjoins-item {
            border-image: url(images/branch-more.png) 0;}

        QTreeView::branch:!has-children:!has-siblings:adjoins-item {
            border-image: url(images/branch-end.png) 0;}

        QTreeView::branch:has-children:!has-siblings:closed,
        QTreeView::branch:closed:has-children:has-siblings {
            border-image: none;
            image: url(images/branch-closed.png);}

        QTreeView::branch:open:has-children:!has-siblings,
        QTreeView::branch:open:has-children:has-siblings {
            border-image: none;
            image: url(images/branch-open.png);}"""

        self.treewidget_.setStyleSheet(branchstyle)
        self.treewidget_.itemClicked.connect(self.currentitem)
        self.treewidget_.currentItemChanged.connect(self.current_item_changed)

    # @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, QtWidgets.QTreeWidgetItem)
    def current_item_changed(self, current, previous):
        # print('\ncurrent: {}, \nprevious: {}'.format(current, previous))
        print(current.text(0), previous)

    def add(self):
        text, ok = QInputDialog.getText(
            self,
            "Add custom section",
            "Enter section geometry f.ex as D325 or just 325 in mm: ",
        )

        if ok:
            self.secondchilditem = QTreeWidgetItem(["%s" % text])
            self.secondparentitem.insertChild(0, self.secondchilditem)
            self.treewidget_.expandItem(self.secondparentitem)
            self.gettext = text

        print(self.secondparentitem.child(0), self.gettext)

    def delete(self):
        self.secondparentitem.removeChild(self.secondparentitem.takeChild(0))

    def currentitem(self):
        print(self.treewidget_.currentItem().text(0), self.treewidget_.selectedItems())
        self.itemtext = self.treewidget_.currentItem().text(0)

        if self.itemtext == self.firstparentitem.text(
            0
        ) or self.itemtext == self.secondparentitem.text(0):
            return None
        elif self.itemtext == self.treewidget_.topLevelItem(0).text(0):
            return None
        elif self.itemtext == None:
            return None
        else:
            self.select_circular_section = int(
                self.itemtext.translate({ord("D"): None})
            )
            print(
                self.itemtext,
                self.treewidget_.selectedItems,
                self.select_circular_section,
            )

            area = str(format(3.1416 / 4 * (self.select_circular_section) ** 2, "0.2E"))
            inerti = str(
                format(3.1416 / 64 * pow(self.select_circular_section, 4), "0.2E")
            )

            self.qlabelcirculardiameterselected = QLabel("")
            qlabelcircularareaselected = QLabel("")
            qlabelcircularinertimomentselected = QLabel("")
            emptylabel1 = QLabel("     ")

            self.qlabelcirculardiameterselected.setText(
                "%s    mm " % self.select_circular_section
            )
            qlabelcircularareaselected.setText("{}    mm2 ".format(area))
            qlabelcircularinertimomentselected.setText("%s    mm4 " % (inerti))

            qlabelhboxgridselected = QGridLayout()
            qlabelhboxgridselected.addWidget(emptylabel1, 0, 0)
            qlabelhboxgridselected.addWidget(self.qlabelcirculardiameterselected, 1, 0)
            qlabelhboxgridselected.addWidget(qlabelcircularareaselected, 2, 0)
            qlabelhboxgridselected.addWidget(qlabelcircularinertimomentselected, 3, 0)
            qlabelhboxgridselected.addWidget(emptylabel1, 4, 0, 5, 0)

            return (
                print(
                    self.itemtext,
                    self.treewidget_.selectedItems,
                    self.select_circular_section,
                ),
                self.boxlayout.addLayout(qlabelhboxgridselected, 6, 2),
                self.qlabelcirculardiameterselected,
            )

    def addimage(self):
        self.imagelabel = QLabel()
        self.imagelabel.setGeometry(15, 15, 15, 15)

    def hidethiswindow(self):
        if self.itemtext == self.firstparentitem.text(
            0
        ) or self.itemtext == self.secondparentitem.text(0):
            QMessageBox.about(
                self, "Error selection", "Please, select a section not a text"
            )
        elif self.itemtext == self.treewidget_.topLevelItem(0).text(0):
            QMessageBox.about(
                self, "Error selection", "Please, select a section not a text"
            )
        elif self.itemtext == None:
            QMessageBox.about(
                self, "Error selection", "Please, select a section not a text"
            )
        else:
            self.savesetting()
            self.hide()

    def qlabeltodefinesection(self):
        self.qlabelcirculardiameter = QLabel("    D = ")
        self.qlabelcirculararea = QLabel("    A = ")
        self.qlabelcircularinertimoment = QLabel("    I = ")
        self.emptylabel = QLabel("     ")
        self.qlabelhboxgrid = QGridLayout()
        self.qlabelhboxgrid.addWidget(self.emptylabel, 0, 0)
        self.qlabelhboxgrid.addWidget(self.qlabelcirculardiameter, 1, 0)
        self.qlabelhboxgrid.addWidget(self.qlabelcirculararea, 2, 0)
        self.qlabelhboxgrid.addWidget(self.qlabelcircularinertimoment, 3, 0)
        self.qlabelhboxgrid.addWidget(self.emptylabel, 4, 0, 5, 0)

    def savesetting(self):
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        # settings = QSettings('config.ini',QSettings.IniFormat)
        settings.beginGroup("D")
        settings.setValue(SETTINGS_TRAY, self.geometry())
        settings.setValue("LineEdit", self.sectionnamecircularindata.text())
        settings.setValue("Selectitem", self.treewidget_.currentItem())
        settings.setValue("Label", self.qlabelcirculardiameterselected)
        settings.endGroup()
        print(
            "Saved",
        )
        # self.hide()

    def loadsetting(self):
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        # settings = QSettings('config.ini',QSettings.IniFormat)
        settings.beginGroup("D")
        myrect = settings.value(SETTINGS_TRAY)
        restorelineEdit = settings.value("LineEdit", "")
        restoreselectsection = settings.value(
            "Selectitem",
        )
        restoreqlabel = settings.value("Label", "")
        self.setGeometry(myrect)
        self.sectionnamecircularindata.setText(restorelineEdit)
        self.treewidget_.setCurrentItem(restoreselectsection)
        settings.endGroup()


if __name__ == "__main__":

    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)
    subwindow = UCircularShape()
    subwindow.show()
    app.exec()