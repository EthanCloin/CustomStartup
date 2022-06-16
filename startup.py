import os
import logging
from logging.config import dictConfig
from pathlib import Path

from config import LOGGING_CONFIG
import sites
from sites import ChromeProfile, SiteInfo
import applications
from applications import AppInfo

dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


class StartupType:
    def __init__(
        self, name: str, apps: list[AppInfo] = None, websites: list[SiteInfo] = None
    ):
        self.name = name
        self.applications = apps
        self.websites = websites

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def open_apps(self):
        applications.open_apps(self.applications)

    def open_websites(self):
        sites.open_all_sites(self.websites)


if __name__ == "__main__":
    sublime_app: AppInfo = AppInfo(
        name="Sublime Text", path=Path("/Applications/Sublime\ " "Text.app")
    )
    support_inbox: SiteInfo = SiteInfo(
        name="Hubspot Inbox",
        url="https://app.hubspot.com/live-messages/3982111/inbox/",
        profile=ChromeProfile.WORK,
    )
    github_home: SiteInfo = SiteInfo(
        name="Github",
        url="https://github.com/ethancloin",
        profile=ChromeProfile.PERSONAL,
    )

    my_apps: list[AppInfo] = [sublime_app]
    my_sites: list[SiteInfo] = [support_inbox, github_home]
    startup_test: StartupType = StartupType(
        name="Test",
        apps=my_apps,
        websites=my_sites,
    )

    startup_test.open_apps()
    startup_test.open_websites()
