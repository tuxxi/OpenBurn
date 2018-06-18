from qtpy.QtWidgets import QMainWindow, QMenuBar, QStatusBar
from qtpy.QtGui import QIcon

class MainWindow(QMainWindow):
    title = "OpenBurn"

    def __init__(self):
        super().__init__(MainWindow, self)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon())
        self.create_default_widgets()

    def create_default_widgets(self):
        self.setMenuBar(QMenuBar())
        self.setStatusBar(QStatusBar())