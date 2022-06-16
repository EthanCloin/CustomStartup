import os
import logging
from logging.config import dictConfig
from config import LOGGING_CONFIG
import sites
from sites import ChromeProfile, SiteInfo
import apps
from apps import AppInfo
dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


class StartupType:
    def __init__(
        self, name: str, applications: list[AppInfo] = None, websites: list[SiteInfo] = None
    ):
        self.name = name
        self.applications = applications
        self.websites = websites

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def open_apps(self):
        apps.open_apps(self.applications)

    def open_websites(self):
        sites.open_all_sites(self.websites)


if __name__ == "__main__":
    pass
