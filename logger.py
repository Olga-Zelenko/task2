import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("logfile.log", encoding="utf-8", mode="w")
logger.addHandler(fileHandler)
formatter = logging.Formatter(
    fmt="%(levelname)s (%(asctime)s) : %(message)s  [%(filename)s] (Line: %(lineno)d)",
    datefmt="%d.%m.%Y %H:%M:%S",
)
fileHandler.setFormatter(formatter)
logger.setLevel(logging.INFO)
