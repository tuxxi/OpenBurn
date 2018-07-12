from typing import Dict
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

        # Dict ordered by propellant name : propellant
        self.propellants: Dict[str: OpenBurnPropellant] = {}
        if filename is not None:
            self.load_database(filename)

    def propellant_names(self):
        return [prop.name for prop in self.propellants]

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

    def clear_database(self) -> None:
        self.propellants.clear()

    def add_propellant(self, propellant: OpenBurnPropellant) -> None:
        self.propellants[propellant.name] = propellant
        self.propellant_added.emit(propellant.name)    # emit signal

    def remove_propellant(self, key: str) -> None:
        """
        Removes a propellant from the database
        :param key: the propellant name to be removed
        """
        self.propellants.pop(key)
        self.propellant_removed.emit(key)   # emit signal

    def update_propellant(self, key: str, new_prop: OpenBurnPropellant) -> None:
        """Updates the propellant database
        :param key: the old propellant's name
        :param new_prop: the new propellant, to replace old_prop
        """
        self.propellants[key] = new_prop
        self.propellant_edited.emit(key)


