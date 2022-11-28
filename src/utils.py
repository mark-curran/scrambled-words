"""Utils for solving the scrambled substring problem."""
import re

from configure_logging import getLogger
from string_wrapper import StringWrapper

logger = getLogger(__name__)


def count_scrambled_substrings(
    dict_dict: dict, input_string: str, dict_lengths: list[int]
) -> int:
    """Count the number of scrambled substrings in an input string.

    Args:
        dict_dict (dict):
            Dictionary of strings to search for.
        input_string (str):
            The string to be searched through.
        dict_lengths (list[int]):
            The lengths of the strings in the dictionary.

    Returns:
        int: Number of scrambled substrings in the input string.
    """
    # Initate output variable.
    num_scrambled_substrings = 0

    # Only scrambled strings with length less than the input string can
    # exist as substrings. Restrict search to these.
    relevant_lengths = [k for k in dict_lengths if k <= len(input_string)]

    # Loop over substrings with relevant length.
    for substr_length in relevant_lengths:
        logger.debug("Searching for scrambled substrings of length: %s", substr_length)
        wrapped_substrings = dict_dict[substr_length]

        # Loop over all wrapped substrings with given length.
        for wrapper in wrapped_substrings:
            logger.debug("Checking for scrambled instances of %s", wrapper.base_str)

            if check_for_scrambled_substring(input_string, wrapper):
                logger.debug(
                    "Found scrambled substring of %s, proceeding to next substring.",
                    wrapper.base_str,
                )
                num_scrambled_substrings += 1
                logger.debug(
                    "num_scrambled_substrings incremented to: %s",
                    num_scrambled_substrings,
                )

    return num_scrambled_substrings


def check_for_scrambled_substring(input_string: str, wrapper: StringWrapper) -> bool:
    """Check if a scrambled substring is contained in an input string.

    This function initially searches for the first and last letter of the
    wrapper, and if successful checks the mid array encoding.

    Args:
        input_string (str):
            The input string to be searched through.
        wrapper (StringWrapper):
            The wrapped string that will be searched for.

    Returns:
        bool: True is the scrambled substring is found, False otherwise.
    """
    # Search for instances of the first letter.
    indices_first_letter = [
        match.start()
        for match in re.finditer(pattern=wrapper.first_letter, string=input_string)
    ]
    if not indices_first_letter:
        logger.debug("No instances of first letter %s found.", wrapper.first_letter)
        return False

    # Search for instances of the last letter.
    for idx_first_letter in indices_first_letter:
        logger.debug(
            "First letter %s found in position %s.",
            wrapper.first_letter,
            idx_first_letter,
        )
        idx_last_letter = idx_first_letter + wrapper.length - 1
        logger.debug("Looking for last letter in position %s", idx_last_letter)

        # Break if index of last letter out of range.
        if idx_last_letter >= len(input_string):
            logger.debug(
                "Index position %s exceeds length of input string %s.",
                idx_last_letter,
                len(input_string),
            )
            break

        # Break if letter in input string does not match last letter of wrapper.
        if input_string[idx_last_letter] != wrapper.last_letter:
            logger.debug(
                "In position %s found letter %s which is not equal %s.",
                idx_last_letter,
                input_string[idx_last_letter],
                wrapper.last_letter,
            )
            break

        # Remaining option is the letters match.
        logger.debug(
            "Found last letter %s in posiiton %s",
            wrapper.last_letter,
            idx_last_letter,
        )
        if check_for_substr_permutations(
            str_to_check=input_string[idx_first_letter + 1 : idx_last_letter],
            wrapper=wrapper,
        ):
            # Stop the search and return True if you find a scrambled substring.
            logger.debug(
                "Permutation found between index %s and %s",
                idx_first_letter,
                idx_last_letter,
            )
            return True

    # If you reach this point then no permutations were found.
    return False


def check_for_substr_permutations(str_to_check: str, wrapper: StringWrapper) -> bool:
    """Check for permutations of the middle characters of the wrapper.

    Args:
        str_to_check (str):
            The string to search for permutations in.
        wrapper (StringWrapper):
            The wrapper whose middle characters define the permutation we will
            look for.

    Returns:
        bool: True is permutation is found, False otherwise.
    """
    logger.debug(
        "The middle of the input string is %s. Encoding as array.",
        str_to_check,
    )
    input_array = StringWrapper.str_to_array_encoding(str_to_check)
    if int_arrays_equal(wrapper.mid_array_encoding, input_array):
        return True


def int_arrays_equal(arr_1: list[int], arr_2: list[int]) -> bool:
    """Check if two arrays are equal.

    Args:
        arr_1 (list[int]): An array.
        arr_2 (list[int]): An array

    Returns:
        bool:
            True if all elements of array 1 equal corresponding element in
            array 2.
    """
    for x, y in zip(arr_1, arr_2):  # pylint: disable=invalid-name
        if x != y:
            return False

    return True
