import os
import logging
from dotenv import load_dotenv
from logging.config import dictConfig
from pathlib import Path
from dataclasses import dataclass
from config import LOGGING_CONFIG
from config import configure_selenium


dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)
load_dotenv()
PERSONAL = os.getenv("PERSONAL_CHROME_PROFILE")
WORK = os.getenv("WORK_CHROME_PROFILE")


@dataclass
class AppInfo:
    name: str
    path: Path


@dataclass
class SiteInfo:
    name: str
    url: str


class StartupType:
    def __init__(
        self, name: str, apps: list[AppInfo] = None, websites: list[SiteInfo] = None
    ):
        self.name = name
        self.apps = apps
        self.websites = websites

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def open_apps(self):
        for app in self.apps:
            exit_code: int = os.system(f"open {app.path}")
            _log.debug(f"opened {app.name} with exit code {exit_code}")

    def open_websites(self):
        # need to use selenium to choose between chrome profiles
        pass


if __name__ == "__main__":
    my_app: AppInfo = AppInfo(name="Macdown", path=Path("/Applications/MacDown.app"))
    my_site: SiteInfo = SiteInfo(name="Don't Ask", url="https://dontasktoask.com/")

    basic_test: StartupType = StartupType("Basic")
    configure_selenium(WORK)
