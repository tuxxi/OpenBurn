from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog, QLabel, QVBoxLayout, QSpacerItem

import openburn as ob


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        self.resize(175, 100)
        self.layout = QVBoxLayout()

        title = QLabel('OpenBurn')
        title.setStyleSheet("font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        version = QLabel('Version ' + ob.__version__)
        self.layout.addWidget(version)

        github = QLabel('<a href=https://github.com/tuxxi/OpenBurn>GitHub</a>')
        github.setTextFormat(Qt.RichText)
        github.setTextInteractionFlags(Qt.TextBrowserInteraction)
        github.setOpenExternalLinks(True)
        self.layout.addWidget(github)

        # author
        self.layout.addSpacerItem(QSpacerItem(10, 10))
        auth = QLabel(self.tr("Author:"))
        auth.setStyleSheet("font-weight: bold;")
        auth.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(auth)

        author = f"{ob.__author__}: {ob.__author_email__}"
        self.layout.addWidget(QLabel(author))

        # special thanks
        self.layout.addSpacerItem(QSpacerItem(10, 10))
        thx = QLabel("Special Thanks:")
        thx.setStyleSheet("font-weight: bold;")
        thx.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(thx)
        for thanks in ob.__special_thanks__:
            self.layout.addWidget(QLabel(thanks))

        self.setLayout(self.layout)
