import os
from dotenv import load_dotenv
from enum import Enum
from dataclasses import dataclass
import webbrowser
from webbrowser import GenericBrowser

load_dotenv()


class ChromeProfile(str, Enum):
    PERSONAL = os.getenv("CHROME_PERSONAL_PROFILE")
    WORK = os.getenv("CHROME_WORK_PROFILE")


@dataclass
class SiteInfo:
    name: str
    url: str
    profile: ChromeProfile


# TODO: refactor to not expect profile and instead pull from SiteInfo
def open_all_sites(sites: list[SiteInfo]):
    open_profiles: list = []
    open_browsers: dict = {}

    for site in sites:
        profile_name: str = site.profile.name
        if profile_name not in open_profiles:
            try:
                new_browser: GenericBrowser = open_new_browser_with_profile(site.profile)
                open_browsers[profile_name] = new_browser
                open_profiles.append(profile_name)
            except Exception as err:
                print(err)
        browser: GenericBrowser = open_browsers.get(profile_name)
        browser.open(site.url)

    # check if provided profile has already been used to open anything
    # if not, open a new window with profile and add to list of opened
    # open the url
    pass


def open_new_browser_with_profile(profile: ChromeProfile) -> GenericBrowser:
    open_chrome_cmd: str = (
        f"open --new -b com.google.Chrome --args --profile-directory={profile.value} %s"
    )
    new_chrome_browser: GenericBrowser = webbrowser.get(using=open_chrome_cmd)
    print(type(new_chrome_browser))
    return new_chrome_browser


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
