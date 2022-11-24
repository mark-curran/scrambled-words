"""Configure logging based on environment variables."""
import os
import sys
from logging import DEBUG, INFO, StreamHandler, getLogger

root_logger = getLogger()

# Set log level based on env variable.
if "SCRAMBLED_WORDS_DEBUG_MODE" in os.environ:
    if os.environ["SCRAMBLED_WORDS_DEBUG_MODE"] == "1":
        root_logger.setLevel(DEBUG)
else:
    root_logger.setLevel(INFO)

# Always log to stdout.
root_logger.addHandler(StreamHandler(stream=sys.stdout))
