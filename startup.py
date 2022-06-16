import os
import logging
import webbrowser
from enum import Enum

from dotenv import load_dotenv
from logging.config import dictConfig
from pathlib import Path
from dataclasses import dataclass
from config import LOGGING_CONFIG
from time import sleep

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)
load_dotenv()

PERSONAL = os.getenv("CHROME_PERSONAL_PROFILE")
WORK = os.getenv("CHROME_WORK_PROFILE")


@dataclass
class AppInfo:
    name: str
    cli_cmd: Path or str  # passed to 'open' cmd


class ChromeProfile(str, Enum):
    PERSONAL = PERSONAL
    WORK = WORK


@dataclass
class SiteInfo:
    name: str
    url: str
    profile: ChromeProfile


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
            exit_code: int = os.system(f"open {app.cli_cmd}")
            _log.debug(
                f"opened {app.name} using {app.cli_cmd} with exit code {exit_code}"
            )

    def open_websites(self):

        chrome_cli = (
            f"open --new -b com.google.Chrome --args --profile-directory={self.websites[0].profile} %s"
        )
        webbrowser.get(chrome_cli).open(self.websites[0].url)


if __name__ == "__main__":
    # my_app: AppInfo = AppInfo(name="Macdown", cli_cmd=Path("/Applications/MacDown.app"))
    chrome_personal: AppInfo = AppInfo(
        name="Chrome 1",
        cli_cmd=f"--new -b com.google.Chrome --args --profile-directory={PERSONAL}",
    )
    chrome_work: AppInfo = AppInfo(
        name="Chrome 2",
        cli_cmd=f"--new -b com.google.Chrome --args --profile-directory={WORK}",
    )

    my_site: SiteInfo = SiteInfo(
        name="Don't Ask",
        url="https://dontasktoask.com/",
        profile=ChromeProfile.PERSONAL,
    )

    basic_test: StartupType = StartupType(
        "Basic", [chrome_work, chrome_personal], [my_site]
    )
    # basic_test.open_apps()
    # sleep(3)
    basic_test.open_websites()
