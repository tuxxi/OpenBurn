from qtpy.QtWidgets import (QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
                            QWidget, QFrame, QGroupBox, QLabel, QSizePolicy,
                            QSplitter, QTableView, QPushButton, QToolButton,
                            QGraphicsView, QGraphicsScene)

from qtpy.QtCore import Qt


class DesignTab(QWidget):
    def __init__(self):
        super(DesignTab, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        sp = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setSizePolicy(sp)

        def setup_grain_design():
            # grain table view
            master = QHBoxLayout(self)
            master.addWidget(QTableView())

            # grain design controls
            controls = QVBoxLayout(self)
            # add a push button
            self.btn_new_grain = QPushButton(self.tr("New Grain"))
            self.btn_new_grain.setMinimumHeight(50)
            controls.addWidget(self.btn_new_grain)

            # add a dividing line
            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            controls.addSpacing(5)
            controls.addWidget(line)

            # rest of the controls buttons
            self.btn_edit_grain = QPushButton(self.tr("Edit"))
            self.btn_edit_grain.setMinimumHeight(30)
            controls.addWidget(self.btn_edit_grain)
            self.btn_delete_Grain = QPushButton(self.tr("Delete"))
            self.btn_delete_Grain.setMinimumHeight(30)
            controls.addWidget(self.btn_delete_Grain)

            # move grain up and down
            moveup = QHBoxLayout()
            self.btn_move_up = QToolButton()
            self.btn_move_up.setArrowType(Qt.UpArrow)
            moveup.addWidget(self.btn_move_up)
            moveup.addWidget(QLabel(self.tr("Move Up")))
            controls.addLayout(moveup)

            movedown = QHBoxLayout()
            self.btn_move_down = QToolButton()
            self.btn_move_down.setArrowType(Qt.DownArrow)
            movedown.addWidget(self.btn_move_down)
            movedown.addWidget(QLabel(self.tr("Move Down")))
            controls.addLayout(movedown)
            controls.addStretch()

            # add info for motor design
            fl_propellant_info = QFormLayout()
            gb_motor_info = QGroupBox(self.tr("Propellant Info"))
            gb_motor_info.setLayout(fl_propellant_info)

            self.lbl_num_grains = QLabel()
            fl_propellant_info.addRow(QLabel(self.tr("Number of Segments:")), self.lbl_num_grains)
            self.lbl_motor_dia = QLabel()
            fl_propellant_info.addRow(QLabel(self.tr("Motor Diameter:")), self.lbl_motor_dia)
            self.lbl_motor_len = QLabel()
            fl_propellant_info.addRow(QLabel(self.tr("Propellant Length:")), self.lbl_motor_len)
            self.lbl_prop_mass = QLabel()
            fl_propellant_info.addRow(QLabel(self.tr("Propellant Mass:")), self.lbl_prop_mass)
            self.lbl_volume_loading = QLabel()
            fl_propellant_info.addRow(QLabel(self.tr("Volume Loading:")), self.lbl_volume_loading)

            # set group box's layout
            controls.addWidget(gb_motor_info)

            # setup master layout
            master.addLayout(controls)
            self.gb_design = QGroupBox(self.tr("Grain Design"))
            self.gb_design.setLayout(master)

        def setup_chamber_design():
            # master layout
            master = QVBoxLayout()
            # master group box
            self.gb_chamber = QGroupBox(self.tr("Chamber Design"))

            # nozzle settings button
            self.btn_nozzle_settings = QPushButton(self.tr("Edit Nozzle"))
            self.btn_nozzle_settings.setMinimumHeight(50)
            master.addWidget(self.btn_nozzle_settings)

            # nozzle info pane
            fl_nozzle_info = QFormLayout()
            gb_nozzle = QGroupBox(self.tr("Nozzle Info"))
            gb_nozzle.setLayout(fl_nozzle_info)

            self.lbl_nozzle_throat = QLabel()
            fl_nozzle_info.addRow(QLabel(self.tr("Throat Diameter:")), self.lbl_nozzle_throat)
            self.lbl_nozzle_exit = QLabel()
            fl_nozzle_info.addRow(QLabel(self.tr("Exit Diameter:")), self.lbl_nozzle_exit)
            self.lbl_nozzle_expansion_ratio = QLabel()
            fl_nozzle_info.addRow(QLabel(self.tr("Expansion Ratio:")), self.lbl_nozzle_expansion_ratio)
            # add group box to master
            master.addWidget(gb_nozzle)
            master.addStretch()

            # overall motor info pane
            fl_motor_info = QFormLayout()
            gb_motor = QGroupBox(self.tr("Motor Info"))
            gb_motor.setLayout(fl_motor_info)

            self.lbl_kn = QLabel()
            fl_motor_info.addRow(QLabel(self.tr("Kn:")), self.lbl_kn)
            self.lbl_port_throat = QLabel()
            fl_motor_info.addRow(QLabel(self.tr("Port/Throat Ratio:")), self.lbl_port_throat)

            master.addWidget(gb_motor)
            self.gb_chamber.setLayout(master)

        def setup_gfx_ui():
            # design overview
            self.motor_display_view = QGraphicsView()
            self.motor_display_scene = QGraphicsScene()
            self.motor_display_view.setScene(self.motor_display_scene)
            self.motor_display_view.show()

            # sliced cross section
            self.grain_slice_view = QGraphicsView()
            self.grain_slice_scene = QGraphicsScene()
            self.grain_slice_view.setScene(self.grain_slice_scene)
            self.grain_slice_view.show()

            # splitter
            self.splt_gfx = QSplitter(Qt.Horizontal)
            self.splt_gfx.addWidget(self.motor_display_view)
            self.splt_gfx.addWidget(self.grain_slice_view)
            self.splt_gfx.setStretchFactor(0, 10)
            self.splt_gfx.setStretchFactor(1, 3)
            self.splt_gfx.setMinimumHeight(50)

        setup_grain_design()
        setup_chamber_design()
        setup_gfx_ui()

        self.splt_grain_design = QSplitter(Qt.Horizontal)
        self.splt_grain_design.addWidget(self.gb_design)
        self.splt_grain_design.addWidget(self.gb_chamber)
        self.splt_grain_design.setStretchFactor(0, 10)
        self.splt_grain_design.setStretchFactor(1, 3)

        self.splt_main = QSplitter(Qt.Vertical)
        self.splt_main.addWidget(self.splt_grain_design)
        self.splt_main.addWidget(self.splt_gfx)
        self.splt_main.setSizes([300, 150])

        layout = QVBoxLayout()
        layout.addWidget(self.splt_main)
        self.setLayout(layout)