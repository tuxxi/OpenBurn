from typing import List
import jsonpickle

from qtpy.QtCore import QObject, Signal

from openburn.core.propellant import OpenBurnPropellant


class PropellantDatabase(QObject):
    database_ready = Signal()
    propellant_added = Signal(str)
    propellant_edited = Signal(str)
    propellant_removed = Signal(str)

    def __init__(self, filename: str = None):
        super(PropellantDatabase, self).__init__()
        self.propellants: List[OpenBurnPropellant] = []
        self.database_filename = filename
        if self.database_filename is not None:
            self.load_database(filename)

    def load_database(self, filename: str):
        self.clear_database()
        with open(filename, 'r') as f:
            data = f.read()
            if len(data) > 0:
                self.propellants = jsonpickle.decode(data)
        self.database_filename: str = filename
        self.database_ready.emit()

    def save_database(self):
        with open(self.database_filename, 'w+') as f:
            if len(self.propellants) > 0:
                jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
                f.write(jsonpickle.encode(self.propellants))

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


