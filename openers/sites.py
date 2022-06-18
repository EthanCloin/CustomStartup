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
            try:
                new_browser: GenericBrowser = open_new_browser_with_profile(site.profile)
                open_browsers[profile_name] = new_browser

            except Exception as err:
                print(err)

            _log.debug(f"added {profile_name} to open browsers")
        open_browsers.get(profile_name).open(site.url)
        _log.debug(f"opened {site.url} under {profile_name}")


def open_new_browser_with_profile(profile: ChromeProfile) -> GenericBrowser:
    open_chrome_cmd: str = (
        f"open --new -b com.google.Chrome --args --profile-directory={profile.value} %s"
    )
    return webbrowser.get(using=open_chrome_cmd)


if __name__ == '__main__':
    my_site: SiteInfo = SiteInfo(
        name="Don't Ask",
        url="https://dontasktoask.com/",
        profile=ChromeProfile.PERSONAL,
    )
    other_site: SiteInfo = SiteInfo(
        name="Don't Ask",
        url="https://dontasktoask.com/",
        profile=ChromeProfile.WORK,
    )

    open_all_sites([my_site, other_site])
