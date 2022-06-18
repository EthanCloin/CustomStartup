import os
from dataclasses import dataclass
from pathlib import Path
import logging

_log = logging.getLogger(__name__)


@dataclass
class AppInfo:
    name: str
    path: Path or str  # passed to 'open' cmd


def open_apps(apps: list[AppInfo]) -> bool:

    for app in apps:
        exit_code: int = os.system(f"open {app.path}")
        _log.debug("opened {} with exit code {}".format(app.name, exit_code))

    exit_codes: list[int] = [os.system(f"open {app.path}") for app in apps]
    return all(code == 0 for code in exit_codes)


if __name__ == "__main__":
    pass
