import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from time import sleep


def configure_selenium(chrome_profile: str):

    options = ChromeOptions()
    options.add_argument(f"--profile-directory={chrome_profile}")
    options.add_argument(f"--user-data-dir={chrome_profile}")

    print(options.arguments)

    driver = webdriver.Chrome(
        options=options,
        executable_path="/Users/ethancloin/Developer/PortfolioProjects/selenium/chromedriver.exe",
        service=Service(ChromeDriverManager().install()),
    )
    driver.get("https://www.google.com")
    sleep(5)
    driver.quit()


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "brief": {"format": "[%(levelname)-7s]: %(message)s"},
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "verbose": {
            "format": "%(asctime)s [%(levelname)s] %(name)s {%(funcName)s}: %(message)s"
        },
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "brief",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "debug": {
            "level": "DEBUG",
            "formatter": "verbose",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["default"],
            "level": "WARNING",
            "propagate": False,
        },
        "sample_pkg": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "__main__": {
            "handlers": ["debug"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
