import logging
from logging.config import dictConfig

from config import LOGGING_CONFIG
from openers import applications, sites
from openers.sites import ChromeProfile, SiteInfo
from openers.applications import AppInfo

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
    pass


# define sites to open
github_home = SiteInfo(
    name="Github",
    url="https://github.com/ethancloin",
    profile=ChromeProfile.PERSONAL,
)
support_inbox = SiteInfo(
    name="Hubspot Inbox",
    url="https://app.hubspot.com/live-messages/3982111/inbox/",
    profile=ChromeProfile.WORK,
)
work_email_inbox = SiteInfo(
    name="Hazlnut Gmail Inbox",
    url="https://mail.google.com/mail/u/0/#inbox",
    profile=ChromeProfile.WORK,
)
support_manual_doc = SiteInfo(
    name="Hazlnut Support Manual",
    url="https://docs.google.com/document/d/1w9eYWqIgOo4wgm5GJZKucFdbEk0c1k8STMzKE5E6dhI/edit",
    profile=ChromeProfile.WORK,
)

# define apps to open
slack = AppInfo(
    name="Slack",
    path="/Applications/Slack.app",
)
notion = AppInfo(
    name="Notion",
    path="/Applications/Notion.app",
)
data_grip = AppInfo(
    name="DataGrip",
    path="/Applications/DataGrip.app",
)
pycharm = AppInfo(
    name="PyCharm",
    path="/Applications/PyCharm.app",
)
one_password = AppInfo(
    name="1Password",
    path="/Applications/1Password\ 7.app",
)

WORK_BASICS = StartupType(
    name="Work Basics",
    websites=[github_home, support_inbox, support_manual_doc, work_email_inbox],
    apps=[slack, notion, data_grip, pycharm, one_password],
)
