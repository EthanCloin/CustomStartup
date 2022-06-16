from openers import applications, sites
from openers.startup import StartupType, SiteInfo, AppInfo, ChromeProfile

if __name__ == '__main__':
    new_start = StartupType("mine", [], [])
    new_app = AppInfo("myapp", "")
    new_site = SiteInfo("mysite", "", ChromeProfile.WORK)

    print("L)")
