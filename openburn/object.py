import uuid
import json

from qtpy.QtCore import QObject


class OpenBurnObject(QObject):
    """Base class of all OpenBurn motor objects.
    Handles json serialization and deserialization as well as uuid creation"""
    def __init__(self):
        super(OpenBurnObject, self).__init__()
        self.uuid = uuid.uuid4()

    def save_json(self) -> json.JSONEncoder:
        """recursively dumps the entire class structure into json"""
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
