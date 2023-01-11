import json
from dataclasses import dataclass, field
from openers.apps import AppInfo
from openers.sites import SiteInfo
from openers.startup import StartupType
import logging
from logging.config import dictConfig
from config import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


@dataclass
class StartupJson:
    """represents the format of the json file which serves as primary storage"""

    startup_modes: list[StartupType] = field(init=True)
    mode_names: list[str] = field(init=False)

    def __post_init__(self):
        self.mode_names = [startup.name for startup in self.startup_modes]

    def fetch_startup(self, mode_name: str) -> StartupType:
        """return startup_mode with provided name if it exists"""

        if mode_name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % mode_name)

        return [mode for mode in self.startup_modes if mode.name == mode_name][0]

    def store_startup(self, mode: StartupType) -> None:
        """adds startup_mode to file if one does not already exist under its name"""
        if mode.name in self.mode_names:
            raise KeyError("startup mode '%s' already exists!" % mode.name)

        self.startup_modes.append(mode)
        self.mode_names.append(mode.name)

    def update_startup(self, prev_name: str, updated_mode: StartupType):
        if prev_name not in self.mode_names:
            raise KeyError("startup mode '%s' does not exist!" % prev_name)


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
