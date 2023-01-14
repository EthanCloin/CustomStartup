from __future__ import annotations
from dataclasses import field, dataclass
from openers.startup import StartupType
import logging
from logging.config import dictConfig
from config import LOGGING_CONFIG, STORAGE_PATH
import pickle

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


@dataclass
class StartupProfile:
    """provides user local storage of their startup types"""

    startup_modes: list[StartupType] = field(init=True)
    mode_names: list[str] = field(init=False)
    # ensure anytime a startup_mode is removed, its name
    # is also removed. a computed property like in vue would
    # be nice.

    def __post_init__(self):
        self.mode_names = [startup.name for startup in self.startup_modes]

    def store_startup(self, mode: StartupType) -> None:
        """adds startup_mode to file if one does not already exist under its name"""
        if mode.name in self.mode_names:
            raise KeyError("startup mode '%s' already exists!" % mode.name)

        self.startup_modes.append(mode)
        self.mode_names.append(mode.name)
        _log.debug("stored %s" % repr(mode))

    def fetch_startup(self, mode: StartupType) -> StartupType:
        """return startup_mode with provided name if it exists"""

        if mode.name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % mode_name)

        return [mode for mode in self.startup_modes if mode.name == mode_name][0]

    def remove_startup(self, mode: StartupType) -> None:
        """removes startup_mode if it exists"""
        if mode.name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % mode_name)

        self.startup_modes.remove(mode)
        self.mode_names.remove(mode.name)
        _log.debug("removed %s" % mode)

    # TODO: fix this to accomodate the change to 'remove_startup'.
    #   either add the ability to remove by name, or handle the mapping
    #   of name-->mode in this fxn.
    # def update_startup(self, prev_name: str, updated_mode: StartupType):
    #     try:
    #         self.remove_startup(prev_name)
    #         self.store_startup(updated_mode)
    #     except KeyError as err:
    #         _log.exception("unable to update startup '%s' " % prev_name)
    #         raise

    # def as_json(self):
    #     """convert each component to its dict form,

    #     (dependent on added schema from marshmallow_dataclass)"""

    #     return [pickle.dump(mode) for mode in self.startup_modes]

    def save_to_file(self):
        # easiest way at first will be just overwrite every time
        with open(STORAGE_PATH, "wb") as f:
            # remember, pickle is not secure and could allow remote code
            # execution. use a different serialization if you ever expect
            # to support users adding arbitary JSON files for bulk setup
            pickle.dump(self, f)

    @staticmethod
    def read_from_file() -> StartupProfile:
        with open(STORAGE_PATH, "rb") as f:
            from_pickle: StartupProfile = pickle.load(f)
            return from_pickle


"""
{
    startup_modes: [
        first_mode: {
            apps: [
                app_one: {
                    
                }
            ],
            sites: [
                site_one: {

                }
            ]
        },
        second_mode: {
            ...
        }
    ]
}
"""

# assuming that objects passed are validated before this stage
