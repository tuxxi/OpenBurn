import sys
from qtpy.QtWidgets import QApplication

from openburn.ui.mainwindow import MainWindow 
from openburn.application.application import OpenBurnApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    openburn = OpenBurnApplication()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())