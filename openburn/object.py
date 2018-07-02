import uuid
import jsonpickle
from copy import deepcopy

from qtpy.QtCore import QObject


class OpenBurnObject(QObject):
    """Base class of all OpenBurn motor objects.
    Handles json serialization and deserialization as well as uuid creation"""
    def __init__(self):
        super(OpenBurnObject, self).__init__()
        self.uuid = uuid.uuid4()

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for key, value in self.__dict__.items():
            setattr(result, key, deepcopy(value, memo))
        return result

    # we don't want UUID to be saved across sessions, so we implement pickle's __getstate__ and __setstate__
    # and remove 'uuid' from the dict
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['uuid']   # ignore uuid
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)

    @classmethod
    def from_json(cls, data: str) -> 'cls':
        """
        factory method to create an object from json data
        :param data: JSON string, encoded with jsonpickle
        :returns: cls()
        """
        obj = jsonpickle.decode(data)
        obj.uuid = uuid.uuid4()     # generate a new uuid
        return obj

    def to_json(self) -> str:
        """
        recursively dumps the entire class structure into json
        :returns JSON string, encoded with jsonpickle
        """
        jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
        return jsonpickle.encode(self)
