"""Script that creates a solution file to the scrambled strings problem."""
import argparse

from configure_logging import getLogger

# TODO: Use itertools.zip to compare the array encodings.
parser = argparse.ArgumentParser()
parser.add_argument("--dictionary", help="Path to the dictinoary file.")
parser.add_argument("--input", help="Path to the input file.")

logger = getLogger(__name__)


def main():
    args = parser.parse_args()

    logger.debug("The args are %s", args)


if __name__ == "__main__":
    main()
