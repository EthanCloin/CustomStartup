import os
import logging
from logging.config import dictConfig
from pathlib import Path
from dataclasses import dataclass
from config import LOGGING_CONFIG

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


@dataclass
class AppInfo:
    name: str
    path: Path


@dataclass
class WebsiteInfo:
    name: str
    url: str


class StartupType:
    def __init__(
        self, name: str, apps: list[AppInfo] = None, websites: list[WebsiteInfo] = None
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
        pass


if __name__ == "__main__":
    my_app = AppInfo(name="Macdown", path=Path("/Applications/MacDown.app"))
    my_site = WebsiteInfo(name="Don't Ask", url="https://dontasktoask.com/")

    basic_test = StartupType("Basic", [my_app])
    basic_test.open_apps()
