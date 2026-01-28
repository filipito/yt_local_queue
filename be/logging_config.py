import logging
import sys

LOG_FORMAT = "[%(asctime)s] :: %(levelname)10s %(name)s: %(message)s"


def setup_logging(level: int = logging.INFO) -> None:
    """Configure logging for the application.

    Import this module and call setup_logging() once at application startup.
    Then in any module:
        import logging
        MODULE_LOGGER = logging.getLogger(__name__)
        MODULE_LOGGER.info("message")
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()
    root_logger.addHandler(handler)

    # Override uvicorn loggers to use our format
    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        uvicorn_logger = logging.getLogger(logger_name)
        uvicorn_logger.handlers.clear()
        uvicorn_logger.propagate = True
