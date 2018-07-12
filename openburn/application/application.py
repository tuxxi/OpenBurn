from qtpy.QtCore import QObject
from qtpy.QtWidgets import QUndoStack

from openburn.core.motor import OpenBurnMotor
from openburn.application.settings import SettingsDatabase
from openburn.application.propellant_db import PropellantDatabase


class OpenBurnApplication(QObject):
    """
    Encapsulates application context that is shared across many UI
    elements and modules:
        propellant database,
        settings,
        undo stack,
        and current design info
    """
    def __init__(self):
        super(OpenBurnApplication, self).__init__()
        self.motor = OpenBurnMotor()
        self.current_design_filename: str = None

        self.undo_stack = QUndoStack(self)
        self.propellant_db = PropellantDatabase('user/propellants.json')
        self.settings = SettingsDatabase('user/settings.json')

    def reset_design(self):
        self.motor = OpenBurnMotor()

    def save_current_design(self):
        self.save_design(self.current_design_filename)

    def save_design(self, filename: str):
        with open(filename, 'w+') as f:
            data = self.motor.to_json()
            f.write(data)
        self.current_design_filename = filename

    def load_design(self, filename: str):
        with open(filename, 'r') as f:
            data = f.read()
            self.motor = OpenBurnMotor.from_json(data)



