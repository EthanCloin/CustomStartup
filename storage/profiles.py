"""
primary manager of user startup routines. can be initialized with a list of StartupRoutines. 

StartupProfile supports storing, fetching, updating, and removing StartupRoutines.
Also supports saving and reading StartupProfile from a file.
"""


from __future__ import annotations
from dataclasses import field, dataclass
from openers.startup import StartupRoutine
import logging
from logging.config import dictConfig
from config import LOGGING_CONFIG, STORAGE_PATH
import pickle

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


@dataclass
class StartupProfile:
    """provides user local storage of their startup types"""

    startups: list[StartupRoutine] = field(init=True, default_factory=list)

    # this list helps enforce 1 routine per name
    # ensure anytime a startup_mode is removed, its name is also removed.
    # a computed property like in vue would be nice.
    startup_names: list[str] = field(init=False, default_factory=list)

    def __post_init__(self):
        self.startup_names = [s.name for s in self.startups]

    def store_startup(self, startup: StartupRoutine) -> None:
        """adds startup_mode to instance if one does not already exist under its name"""
        if startup.name in self.startup_names:
            raise KeyError("startup '%s' already exists!" % startup.name)

        self.startups.append(startup)
        self.startup_names.append(startup.name)
        _log.debug("stored %s" % repr(startup))

    def fetch_startup(
        self, routine: StartupRoutine = None, routine_name: str = ""
    ) -> StartupRoutine:
        """return startup_mode with provided routine object or name if it exists"""

        target_name = ""
        target_name = routine.name if routine else routine_name

        if target_name not in self.startup_names:
            raise KeyError("startup mode '%s' does not exist!" % target_name)

        return [s for s in self.startups if s.name == target_name][0]

    def remove_startup(self, routine: StartupRoutine) -> None:
        """removes startup_mode if it exists"""
        if routine.name not in self.startup_names:
            raise KeyError("startup mode '%s' does not exist!" % routine.name)

        self.startups.remove(routine)
        self.startup_names.remove(routine.name)
        _log.debug("removed %s" % routine.name)

    # TODO: fix this to accomodate the change to 'remove_startup'.
    #   either add the ability to remove by name, or handle the mapping
    #   of name-->mode in this fxn.
    def update_startup(self, updated_routine: StartupRoutine, prev_name: str = ""):
        """updates the routine to match provided object. include prev_name parameter if the
        name value has changed"""

        # ensure previous version is removed when updated version has a different name
        if prev_name and prev_name != updated_routine.name:
            old_routine = self.fetch_startup(routine_name=prev_name)
            self.remove_startup(old_routine)
        else:
            old_routine = self.fetch_startup(routine_name=updated_routine.name)
            self.remove_startup(old_routine)

        self.store_startup(updated_routine)
        _log.debug("replaced %s with %s" % (old_routine, updated_routine))

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
