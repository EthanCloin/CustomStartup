import logging
from logging.config import dictConfig

from config import LOGGING_CONFIG
from openers import apps, sites
from openers.sites import ChromeProfile, SiteInfo
from openers.apps import AppInfo

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

    def run_startup(self):
        apps.open_apps(self.applications)
        sites.open_all_sites(self.websites)

# SITES
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
    name="Hazlnut Gmail",
    url="https://mail.google.com/mail/u/0/#inbox",
    profile=ChromeProfile.WORK,
)
support_manual_doc = SiteInfo(
    name="Hazlnut Support Manual",
    url="https://docs.google.com/document/d/1w9eYWqIgOo4wgm5GJZKucFdbEk0c1k8STMzKE5E6dhI/edit",
    profile=ChromeProfile.WORK,
)
personal_email = SiteInfo(
    name="Personal Gmail",
    url="https://mail.google.com/mail/u/0/#inbox",
    profile=ChromeProfile.WORK,
)

# APPS
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
flycut = AppInfo(
    name="Flycut Clipboard",
    path="/Applications/Flycut.app",
)
discord = AppInfo(
    name="Discord",
    path="/Applications/Discord.app",
)

# STARTUPS
WORK_BASICS = StartupType(
    name="Work Basics",
    websites=[github_home, support_inbox, support_manual_doc, work_email_inbox],
    applications=[slack, notion, data_grip, pycharm, one_password, flycut],
)
DEFAULT_STARTUP = StartupType(
    name="Default",
    applications=[one_password, flycut, discord],
    websites=[personal_email]
)

if __name__ == "__main__":
    pass
