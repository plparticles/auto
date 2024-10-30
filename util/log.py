from loguru import logger
import sys
from config.log_config import LogPath


class Logs:

    def __init__(self, module_name):
        self.module_name = module_name

    def get_logger(self):
        logger.configure(handlers=[
            {
                "sink": sys.stderr,
                "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} |<lvl>{level:8}</>| {name} : {module}:{line:4} | <cyan>{extra[module_name]}</> | - <lvl>{message}</>",
                "colorize": True
            },
            {
                "sink": LogPath.logs_path,
                "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} |{level:8}| {name} : {module}:{line:4} | {extra[module_name]} | - {message}",
                "colorize": False
            },
        ])

        log = logger.bind(module_name=self.module_name)

        return log


if __name__ == '__main__':
    logger = Logs(__name__).get_logger()
    logger.info("test")