import argparse
from openers.startup import WORK_BASICS


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI tool to open defined sets of websites and apps"
    )
    startup_options = parser.add_mutually_exclusive_group()
    startup_options.add_argument(
        "-w",
        "--work",
        help="flag to startup with WORK preset",
        action="store_true",
        default=True,
    )
    startup_options.add_argument(
        "-p",
        "--personal",
        help="flag to startup with PERSONAL preset",
        action="store_true",
    )
    args: argparse.Namespace = parser.parse_args()
    print(args)

    if args.work:
        print("running")
        WORK_BASICS.open_apps()
        WORK_BASICS.open_websites()
