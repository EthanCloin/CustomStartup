import logging
import logging.config
import argparse
from openers.startup import WORK_BASICS, DEFAULT_STARTUP, TEST_STARTUP
from config import LOGGING_CONFIG
from storage.profiles import StartupProfile


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
    ),
    startup_options.add_argument(
        "-t",
        "--test",
        help="flag to startup with TEST preset",
        action="store_true",
    )
    args: argparse.Namespace = parser.parse_args()
    _log.debug("args: {}".format(args))

    if args.work:
        WORK_BASICS.run_startup()
    elif args.test:
        TEST_STARTUP.run_startup()
    elif args.default:
        DEFAULT_STARTUP.run_startup()


if __name__ == "__main__":
    # main()

    # create instance, save to file, mutate, prove difference
    my_manager = StartupProfile([WORK_BASICS, TEST_STARTUP])
    _log.info("OG1: " + str(my_manager))
    my_manager.save_to_file()
    my_manager.remove_startup(WORK_BASICS)
    _log.info("OG2: " + str(my_manager))

    stored_manager = StartupProfile.read_from_file()
    _log.info("OG: " + str(stored_manager))
