import os
import logging
from dotenv import load_dotenv
from enum import Enum
from dataclasses import dataclass
import webbrowser
from webbrowser import GenericBrowser

load_dotenv()
_log = logging.getLogger(__name__)


class ChromeProfile(str, Enum):
    PERSONAL = os.getenv("CHROME_PERSONAL_PROFILE")
    WORK = os.getenv("CHROME_WORK_PROFILE")


@dataclass
class SiteInfo:
    name: str
    url: str
    profile: ChromeProfile


def open_all_sites(sites: list[SiteInfo]):
    open_browsers: dict = {}

    for site in sites:
        profile_name: str = site.profile.name
        if profile_name not in open_browsers.keys():
            new_browser: GenericBrowser = open_new_browser_with_profile(
                site.profile
            )
            # store opened browsers in dictionary using profile_name as key
            open_browsers[profile_name]: GenericBrowser = new_browser
        open_browsers.get(profile_name).open(site.url)
        _log.info("opened {} under {}".format(site.url, profile_name))


def open_new_browser_with_profile(profile: ChromeProfile) -> GenericBrowser:
    open_chrome_cmd: str = (
        f"open --new -b com.google.Chrome --args --profile-directory={profile.value} %s"
    )
    return webbrowser.get(using=open_chrome_cmd)


if __name__ == "__main__":
    pass
