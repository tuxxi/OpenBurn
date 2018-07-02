from qtpy.QtCore import QObject
from qtpy.QtWidgets import QUndoStack

from openburn.core.motor import OpenBurnMotor
from openburn.application.settings import SettingsDatabase
from openburn.application.propellant_db import PropellantDatabase


class OpenBurnApplication(QObject):
    def __init__(self):
        super(OpenBurnApplication, self).__init__()
        self.motor = OpenBurnMotor()
        self.current_design_filename: str = None

        self.undo_stack = QUndoStack(self)
        self.propellant_db = PropellantDatabase('user/propellants.json')
        self.settings = SettingsDatabase('user/settings.json')

    def reset_design(self):
        pass

    def save_current_design(self):
        self.save_design(self.current_design_filename)

    def save_design(self, filename: str):
        pass

    def load_design(self, filename: str):
        pass



