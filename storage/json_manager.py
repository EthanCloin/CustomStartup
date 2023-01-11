import json
from dataclasses import dataclass, field
from openers.apps import AppInfo
from openers.sites import SiteInfo
from openers.startup import StartupType
import logging
from logging.config import dictConfig
from config import LOGGING_CONFIG, STORAGE_PATH
from pathlib import Path


dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


@dataclass
class StartupJson:
    """represents the format of the json file which serves as primary storage"""

    startup_modes: list[StartupType] = field(init=True)
    mode_names: list[str] = field(init=False)

    def __post_init__(self):
        self.mode_names = [startup.name for startup in self.startup_modes]

    def store_startup(self, mode: StartupType) -> None:
        """adds startup_mode to file if one does not already exist under its name"""
        if mode.name in self.mode_names:
            raise KeyError("startup mode '%s' already exists!" % mode.name)

        self.startup_modes.append(mode)
        self.mode_names.append(mode.name)
        _log.debug("stored %s" % repr(mode))

    def fetch_startup(self, mode_name: str) -> StartupType:
        """return startup_mode with provided name if it exists"""

        if mode_name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % mode_name)

        return [mode for mode in self.startup_modes if mode.name == mode_name][0]

    def remove_startup(self, mode_name: str) -> None:
        """removes startup_mode if it exists"""
        if mode_name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % mode_name)

        target_mode = self.fetch_startup(mode_name)
        self.startup_modes.remove(target_mode)
        self.mode_names.remove(mode_name)
        _log.debug("removed %s" % repr(target_mode))

    def update_startup(self, prev_name: str, updated_mode: StartupType):
        try:
            self.remove_startup(prev_name)
            self.store_startup(updated_mode)
        except KeyError as err:
            _log.exception("unable to update startup '%s' " % prev_name)
            raise

    def save_to_file(self):
        # easiest way at first will be just overwrite every time
        # maybe eventually i should have it load and diff to update
        pass


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
