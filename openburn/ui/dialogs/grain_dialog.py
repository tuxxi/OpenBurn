from qtpy.QtWidgets import (QDialog, QGroupBox, QGridLayout, QHBoxLayout, QVBoxLayout, QFrame,
                            QComboBox, QLabel, QPushButton)
from qtpy.QtGui import QIcon

from openburn.application import app_context
from openburn import RESOURCE_PATH


class NewGrainDialog(QDialog):
    def __init__(self):
        super(NewGrainDialog, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Add New Grain")
        self.setWindowIcon(QIcon(RESOURCE_PATH + "icons/nakka-finocyl.gif"))

        self.resize(400, 400)

        controls = QGridLayout()
        gb_frame = QGroupBox(self.tr("Grain Design"))
        gb_frame.setLayout(controls)
        
        self.cb_grain_type = QComboBox()

        # TODO: make grain types auto propagate combobox
        self.cb_grain_type.addItems([self.tr("Cylindrical (BATES)")])
        controls.addWidget(QLabel(self.tr("Core Shape")), 0, 0)
        controls.addWidget(self.cb_grain_type, 0, 1)

        self.cb_propellant_type = QComboBox()
        self.cb_propellant_type.addItems(app_context.propellant_db.propellant_names())
        controls.addWidget(QLabel(self.tr("Propellant Type")), 1, 0)
        controls.addWidget(self.cb_propellant_type, 1, 1)

        # ok and cancel buttons
        btn_ok = QPushButton(self.tr("Apply"))
        btn_ok.clicked.connect(self.confirm_grain)
        btn_cancel = QPushButton(self.tr("Close"))
        btn_cancel.clicked.connect(self.close)

        lay_btns = QHBoxLayout()
        lay_btns.addWidget(btn_ok)
        lay_btns.addWidget(btn_cancel)
        frame_btns = QFrame()
        frame_btns.setLayout(lay_btns)

        # master layout
        master = QVBoxLayout()
        master.addWidget(gb_frame)
        master.addSpacing(10)
        master.addWidget(frame_btns)
        self.setLayout(master)

    def confirm_grain(self):
        # grain = OpenBurnGrain.from_widget_factory(...)
        pass
