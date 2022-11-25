"""Script that creates a solution file to the scrambled strings problem."""
import argparse

from configure_logging import getLogger
from string_wrapper import StringWrapper
from utils import count_scrambled_substrings

parser = argparse.ArgumentParser()
parser.add_argument("--dictionary", help="Path to the dictinoary file.", required=True)
parser.add_argument("--input", help="Path to the input file.", required=True)

logger = getLogger(__name__)


def main():
    """Run the sequence of steps to produce a solution."""
    args = parser.parse_args()
    logger.debug("The args are %s", args)

    # We need to wrap the dictionary file as an actual dictioary.
    dict_dict = {}

    with open(args.dictionary, "r", encoding="utf-8") as file:
        for j, line in enumerate(file.readlines()):
            logger.debug(f"The {j}-th line is: {line.rstrip()}")
            wrapper = StringWrapper(line.rstrip())
            length = wrapper.length

            if length not in dict_dict:
                logger.debug("Encountered first string of length %s", length)
                dict_dict[length] = []

            logger.debug(f"Appending {j}-th wrapped string to dict_dict.")
            dict_dict[wrapper.length].append(wrapper)

    # We need the input strings as a dictionary.
    list_input = []

    with open(args.input, "r", encoding="utf-8") as file:
        for j, line in enumerate(file.readlines()):
            logger.debug(f"The {j}-th line is: {line.rstrip()}")
            list_input.append(line.rstrip())

    dict_lengths = list(dict_dict)

    count_scrambled_substrings(dict_dict, list_input, dict_lengths)

    # TODO: Format output.


if __name__ == "__main__":
    main()
