"""Script that creates a solution file to the scrambled strings problem."""
import argparse

from configure_logging import getLogger
from string_wrapper import StringWrapper
from utils import count_scrambled_substrings

parser = argparse.ArgumentParser()
parser.add_argument("--dictionary", help="Path to the dictinoary file.", required=True)
parser.add_argument("--input", help="Path to the input file.", required=True)

logger = getLogger(__name__)


def main(dictionary_path: str, input_path: str) -> None:
    """Count number of scrambled substrings in an input file.

    Args:
        dictionary_path (str):
            Path to the dictionary file with the strings that we will look for.
        input_path (str):
            Path to the input file with the strings we will look through.
    """
    # A place to store the wrappers from our dictionary, keys are the length
    # of each wrapper.
    dict_dict = {}

    # Generate the wrappers.
    with open(dictionary_path, "r", encoding="utf-8") as file:
        for j, line in enumerate(file.readlines()):
            # Use .rstrip() to get rid of the new line character.
            logger.debug(f"The {j}-th line is: {line.rstrip()}")
            wrapper = StringWrapper(line.rstrip())
            length = wrapper.length

            if length not in dict_dict:
                logger.debug("Encountered first string of length %s", length)
                dict_dict[length] = []

            logger.debug(f"Appending {j}-th wrapped string to dict_dict.")
            dict_dict[wrapper.length].append(wrapper)

    # Get the lengths of the wrappers as a separate list.
    dict_lengths = list(dict_dict)

    # We also need the input strings as a dictionary.
    list_input = []
    with open(input_path, "r", encoding="utf-8") as file:
        for j, line in enumerate(file.readlines()):
            logger.debug(f"The {j}-th line is: {line.rstrip()}")
            list_input.append(line.rstrip())

    # Initiate our output.
    output_str = ""

    # Search the inputs for scrambled strings and format the output.
    for j, input_str in enumerate(list_input):
        num_scrambled_substrings = count_scrambled_substrings(
            dict_dict, input_str, dict_lengths
        )
        logger.debug("Checked for scrambled substrings inside of: %s", input_str)
        logger.debug("Num of scrambled substrings: %s", num_scrambled_substrings)
        output_str = output_str + f"Case: #{j+1} {num_scrambled_substrings}\n"

    # Print solution to stdout.
    print(output_str)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.dictionary, args.input)
