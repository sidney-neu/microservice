import logging
from logging.config import dictConfig

def config_log():
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "loggers": {
                "ml.log": {
                    "level": "INFO",
                    "handlers": ["info_handler", "error_handler"],
                    "propagate": 1,
                    "qualname": "ml.log",
                }
            },
            "handlers": {
                "info_handler": {
                    "level": "INFO",
                    "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                    "filename": "./app/logs/ml_info.log",
                    "maxBytes": 1024 * 1024 * 10,
                    "backupCount": 10,
                    "delay": True,
                    "formatter": "default",
                },
                "error_handler": {
                    "level": "ERROR",
                    "class": "concurrent_log_handler.ConcurrentRotatingFileHandler",
                    "filename": "./app/logs/ml_error.log",
                    "maxBytes": 1024 * 1024 * 10,
                    "backupCount": 10,
                    "delay": True,
                    "formatter": "detail",
                },
            },
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s: %(message)s",
                    "datefmt": "[%Y-%m-%d %H:%M:%S]",
                    "class": "logging.Formatter",
                },
                "detail": {
                    "format": "[%(asctime)s] %(levelname)s in %(pathname)s %(lineno)s: %(message)s",
                    "datefmt": "[%Y-%m-%d %H:%M:%S]",
                    "class": "logging.Formatter",
                },
            },
        }
    )
    logger = logging.getLogger("ml.log")
