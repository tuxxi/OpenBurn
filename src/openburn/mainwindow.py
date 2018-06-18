from qtpy.QtWidgets import QMainWindow, QMenuBar, QStatusBar
from qtpy import QtGui


class MainWindow(QMainWindow):
    """OpenBurn's main window"""
    title = "OpenBurn"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QtGui.QIcon(":/icons/nakka-finocyl.gif"))
        self.create_default_widgets()

    
    def create_default_widgets(self):
        def create_menubar():
            self.menubar = QMenuBar()
            self.file_sub_menu = self.menubar.addMenu('File')
            self.edit_dub_menu = self.menubar.addMenu('Edit')
            self.edit_dub_menu = self.menubar.addMenu('Tools')
            self.edit_dub_menu = self.menubar.addMenu('Help')

        def create_statusbar():
            self.statusbar = QStatusBar()
            self.statusbar.showMessage("Ready", 0)

        create_menubar()
        self.setMenuBar(self.menubar)

        create_statusbar()
        self.setStatusBar(self.statusbar)

