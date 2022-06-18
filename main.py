import logging
import logging.config
import argparse
from openers.startup import WORK_BASICS, DEFAULT_STARTUP
from config import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
_log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to open defined sets of websites and apps"
    )
    startup_options = parser.add_mutually_exclusive_group()
    startup_options.add_argument(
        "-w",
        "--work",
        help="flag to startup with WORK preset",
        action="store_true",
    )
    # startup_options.add_argument(
    #     "-p",
    #     "--personal",
    #     help="flag to startup with PERSONAL preset",
    #     action="store_true",
    # )
    startup_options.add_argument(
        "-d",
        "--default",
        help="flag to startup with DEFAULT preset",
        action="store_true",
        default=True,
    )
    args: argparse.Namespace = parser.parse_args()
    _log.debug("args: {}".format(args))

    if args.work:
        WORK_BASICS.run_startup()
    elif args.default:
        DEFAULT_STARTUP.run_startup()


if __name__ == "__main__":
    main()
