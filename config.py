from pathlib import Path

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "brief": {"format": "[%(levelname)s]: %(message)s"},
        "standard": {
            "format": "[%(levelname)s]: %(message)s (%(funcName)s) %(asctime)s"
        },
        "verbose": {
            "format": "[%(levelname)s]: %(message)s {%(name)s} (%(funcName)s) %(asctime)s "
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
        "openers": {"handlers": ["debug"], "level": "DEBUG", "propagate": False},
        "storage": {"handlers": ["debug"], "level": "DEBUG", "propagate": False},
        "__main__": {
            "handlers": ["debug"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
STORAGE_PATH = Path("storage/user_startups.pickle")
