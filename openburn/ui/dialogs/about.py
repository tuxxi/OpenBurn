from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QLabel, QVBoxLayout, QSpacerItem

from openburn import __version__


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        self.resize(175, 100)

        text = QLabel('OpenBurn')
        text.setStyleSheet("font-weight: bold;")
        text.setAlignment(Qt.AlignCenter)

        version = QLabel('Version ' + __version__)

        github = QLabel('<a href=https://github.com/tuxxi/OpenBurn>GitHub</a>')
        github.setTextFormat(Qt.RichText);
        github.setTextInteractionFlags(Qt.TextBrowserInteraction);
        github.setOpenExternalLinks(True);

        self.layout = QVBoxLayout()
        self.layout.addWidget(text)
        self.layout.addWidget(version)
        self.layout.addWidget(github)

        authors = ['tuxxi: aidan@sojourner.me'     # .. add more later?
                   ]
        special_thanks = ['John Wickman',
                          'Peter Hackett'
                          ]
        # authors
        self.layout.addSpacerItem(QSpacerItem(10, 10))
        auth = QLabel("Authors:")
        auth.setStyleSheet("font-weight: bold;")
        auth.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(auth)
        for author in authors:
            self.layout.addWidget(QLabel(author))

        # special thanks
        self.layout.addSpacerItem(QSpacerItem(10, 10))
        thx = QLabel("Special Thanks:")
        thx.setStyleSheet("font-weight: bold;")
        thx.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(thx)
        for thanks in special_thanks:
            self.layout.addWidget(QLabel(thanks))

        self.setLayout(self.layout)
