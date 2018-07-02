from typing import List
import jsonpickle

from qtpy.QtCore import QObject, Signal

from openburn.core.propellant import OpenBurnPropellant


class PropellantDatabase(QObject):
    propellant_added = Signal(str)
    propellant_edited = Signal(str)
    propellant_removed = Signal(str)

    def __init__(self, filename: str):
        super(PropellantDatabase, self).__init__()
        self.propellants: List[OpenBurnPropellant] = []
        self.database_filename: str = filename

    def load_database(self, filename: str):
        self.propellants = {}
        with open(filename, 'r') as f:
            self.propellants = jsonpickle.decode(f.read())

    def save_database(self):
        with open(self.database_filename, 'w') as f:
            data = jsonpickle.encode(self.propellants)
            f.write(data)

    def clear_database(self):
        self.propellants.clear()

    def add_propellant(self, propellant: OpenBurnPropellant):
        self.propellants.append(propellant)
        self.propellant_added.emit(propellant.name)    # emit signal

    def remove_propellant(self, propellant: OpenBurnPropellant):
        self.propellants.remove(propellant)
        self.propellant_removed.emit(propellant.name)   # emit signal

    def update_propellant(self, old_prop: OpenBurnPropellant, new_prop: OpenBurnPropellant):
        """Updates the propellant database
        :param old_prop: the old propellant
        :param new_prop: the new propellant, to replace old_prop
        """
        index = self.propellants.index(old_prop)
        self.propellants[index] = new_prop
        self.propellant_edited.emit(old_prop.name)


