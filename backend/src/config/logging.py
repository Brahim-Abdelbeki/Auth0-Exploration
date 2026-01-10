import logging
import os
import sys
from datetime import datetime

class ColoredFormatter(logging.Formatter):
    
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    cyan = "\x1b[36m"
    magenta = "\x1b[35m"
    green = "\x1b[32m"

    def format(self, record):
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        
        level_colors = {
            logging.DEBUG: self.green,
            logging.INFO: self.blue,
            logging.WARNING: self.yellow,
            logging.ERROR: self.red,
            logging.CRITICAL: self.bold_red
        }
        
        level_color = level_colors.get(record.levelno, self.reset)
        
        log_message = (
            f"{level_color}{timestamp} [{record.levelname}]{self.reset} "
            f"[{self.cyan}{record.filename}{self.reset}:{record.lineno} "
            f"({self.magenta}{record.funcName}{self.reset})] - "
            f"{record.getMessage()}"
        )
        
        return log_message


class PlainFormatter(logging.Formatter):
    def format(self, record):
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        return (
            f"{timestamp} [{record.levelname}] "
            f"[{record.filename}:{record.lineno} ({record.funcName})] - "
            f"{record.getMessage()}"
        )

logger = logging.getLogger("language_coach")
logger.setLevel(logging.DEBUG)

logger.handlers.clear()

# Use colors only when writing to a TTY (interactive console) and NO_COLOR is not set.
stream = sys.stdout
ch = logging.StreamHandler(stream)
ch.setLevel(logging.DEBUG)

def _truthy(envval: str | None) -> bool:
    if not envval:
        return False
    return envval.strip().lower() in {"1", "true", "yes", "on"}

is_tty = hasattr(stream, "isatty") and stream.isatty()
force_color = _truthy(os.getenv("FORCE_COLOR"))
no_color = _truthy(os.getenv("NO_COLOR"))
use_color = (is_tty and not no_color) or force_color

ch.setFormatter(ColoredFormatter() if use_color else PlainFormatter())
logger.addHandler(ch)