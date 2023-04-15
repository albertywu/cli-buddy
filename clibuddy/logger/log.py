import logging
import sys


def setup_logger(debug: bool = False):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level, stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")


logger = logging.getLogger("clibuddy")
