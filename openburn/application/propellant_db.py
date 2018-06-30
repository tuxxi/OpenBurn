from typing import List
from qtpy.QtCore import QObject

from openburn.core.propellant import OpenBurnPropellant


class PropellantDatabase(QObject):
    def __init__(self):
        super(PropellantDatabase, self).__init__()
        self.propellants: List[OpenBurnPropellant] = []
        self.database_filename: str = None

    def load_database(self, filename: str):
        pass

    def save_database(self):
        pass

    def add_new_propellant(self):
        pass

    def remove_propellant(self, propellant_name: str):
        pass
