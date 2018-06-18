import sys
from qtpy.QtWidgets import QApplication

import resources    # import the compiled resources file from pyrcc5

from openburn.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())