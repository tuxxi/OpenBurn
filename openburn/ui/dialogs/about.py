from qtpy.QtCore import Qt
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QDialog, QLabel, QVBoxLayout, QSpacerItem

from openburn import __version__


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        self.resize(100,100)

        text = QLabel('OpenBurn')
        text.setStyleSheet("font-weight: bold;")
        text.setAlignment(Qt.AlignCenter)

        version = QLabel('Version ' + __version__)

        auth = QLabel("Authors:")
        auth.setStyleSheet("font-weight: bold;")
        auth.setAlignment(Qt.AlignCenter)

        authors = [ QLabel('tuxxi: aidan@sojourner.me')     # .. add more later?
            ]
        github = QLabel('<a href=https://github.com/tuxxi/OpenBurn>GitHub</a>')
        github.setTextFormat(Qt.RichText);
        github.setTextInteractionFlags(Qt.TextBrowserInteraction);
        github.setOpenExternalLinks(True);

        self.layout = QVBoxLayout()
        self.layout.addWidget(text)
        self.layout.addWidget(version)
        self.layout.addWidget(github)

        self.layout.addSpacerItem(QSpacerItem(10, 10))
        self.layout.addWidget(auth)
        for author in authors:
            self.layout.addWidget(author)

        self.setLayout(self.layout)
