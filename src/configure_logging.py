"""Configure logging based on environment variables."""
import os
import sys
from logging import DEBUG, INFO, Formatter, StreamHandler, getLogger

root_logger = getLogger()


# Set log level based on env variable.
if "SCRAMBLED_WORDS_DEBUG_MODE" in os.environ:
    if os.environ["SCRAMBLED_WORDS_DEBUG_MODE"] == "1":
        root_logger.setLevel(DEBUG)
else:
    root_logger.setLevel(INFO)

# Format log messages in desired format.
# Full list of available substitutions:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# TODO: If using multi-threading then add %(threadName)s
formatter = Formatter(fmt="%(levelname)s %(funcName)s %(lineno)d: %(message)s")


# Always log to stdout with desired format.
handler = StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
root_logger.addHandler(handler)
