from qtpy.QtWidgets import (QWidget, QFrame, QMainWindow, QMenuBar, QStatusBar, QAction, QApplication,
                            QTabWidget, QVBoxLayout)

from qtpy.QtGui import QIcon

from openburn import RES
from openburn.ui.dialogs.about import AboutDialog

from openburn.ui.designtab import DesignTab


class MainWindow(QMainWindow):
    """OpenBurn's main window"""
    title = "OpenBurn"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(RES + "icons/nakka-finocyl.gif"))

        self.create_default_widgets()
        self.setup_ui()

    def create_default_widgets(self):
        """Creates static widgets such as menubar and statusbar"""

        def create_menubar():
            """Create menu bar and populate it with sub menu actions"""

            def file_menu():

                """Create a file submenu"""
                self.file_sub_menu = self.menubar.addMenu('File')

                self.open_action = QAction('Open File', self)
                self.open_action.setStatusTip('Open a new design')
                self.open_action.setShortcut('CTRL+O')
                # self.open_action.triggered.connect(self.open_file)

                self.exit_action = QAction('Exit', self)
                self.exit_action.setStatusTip('Exit the application.')
                self.exit_action.setShortcut('CTRL+Q')
                self.exit_action.triggered.connect(QApplication.quit)

                self.file_sub_menu.addAction(self.open_action)
                self.file_sub_menu.addAction(self.exit_action)

            def edit_menu():
                self.edit_dub_menu = self.menubar.addMenu('Edit')

            def tools_menu():
                self.edit_dub_menu = self.menubar.addMenu('Tools')

            def help_menu():
                """Create help submenu"""
                self.help_sub_menu = self.menubar.addMenu('Help')
                self.about_action = QAction('About', self)
                self.about_action.setStatusTip('About the application.')
                self.about_action.setShortcut('CTRL+H')
                self.about_action.triggered.connect(self.about_dialog.exec_)
                self.help_sub_menu.addAction(self.about_action)

            self.menubar = QMenuBar(self)
            file_menu()
            edit_menu()
            tools_menu()
            help_menu()

        def create_statusbar():
            self.statusbar = QStatusBar(self)
            self.statusbar.showMessage("Ready", 0)

        self.about_dialog = AboutDialog(self)

        create_menubar()
        self.setMenuBar(self.menubar)

        create_statusbar()
        self.setStatusBar(self.statusbar)

    def setup_ui(self):
        """setup the tab widget UI"""
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(DesignTab(), "Design")
        self.tab_widget.addTab(QWidget(), "Simulation")
        self.tab_widget.addTab(QWidget(), "Propellants")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.frame = QFrame()
        self.frame.setLayout(self.layout)

        self.setCentralWidget(self.frame)
