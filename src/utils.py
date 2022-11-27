"""Utils for the solving the scrambled substring problem."""
import re

from configure_logging import getLogger
from string_wrapper import StringWrapper

logger = getLogger(__name__)


def count_scrambled_substrings(
    dict_dict: str, list_input: list[str], dict_lengths: list[int]
) -> list[str]:
    """
    Return a list of instances of scrambled substrings from dict_dict in list_input.

    TODO: Update docstring.
    """

    for j, input_string in enumerate(list_input):
        logger.debug("The %s-th input string is %s", j, input_string)
        length_input = len(input_string)

        # Only scrambled strings with length less than the input string can
        # exist as substrings.
        relevant_lengths = [k for k in dict_lengths if k <= length_input]

        for substr_length in relevant_lengths:
            logger.debug(
                "Searching for scrambled substrings of length: %s", substr_length
            )
            wrapped_substrings = dict_dict[substr_length]
            num_scrambled_substrings = 0
            for wrapper in wrapped_substrings:
                logger.debug("Checking for scrambled instances of %s", wrapper.base_str)

                # TODO: Consider running these functions in separate threads.
                if check_for_scrambled_substring(input_string, wrapper):
                    num_scrambled_substrings += 1
                    logger.debug(
                        "Found scrambled substring of %s, proceeding to next substring.",
                        wrapper.base_str,
                    )
                    break


def check_for_scrambled_substring(
    input_string: str, wrapper: StringWrapper
) -> list[int]:
    """Get the indices in input_string that match the last letter of wrapper."""
    output_list = []

    indices_first_letter = sorted(
        [
            match.start()
            for match in re.finditer(pattern=wrapper.first_letter, string=input_string)
        ]
    )
    if not indices_first_letter:
        logger.debug("No instances of first letter found.")
        return output_list

    # Search for instances of the last letter.
    for idx_first_letter in indices_first_letter:
        logger.debug(
            "First letter %s found in position %s.",
            wrapper.first_letter,
            idx_first_letter,
        )
        idx_last_letter = idx_first_letter + wrapper.length - 1
        logger.debug("Looking for last letter in position %s", idx_last_letter)

        # Index of last letter out of range.
        if idx_last_letter >= len(input_string):
            logger.debug(
                "Index position %s exceeds length of input string %s.",
                idx_last_letter,
                len(input_string),
            )
            break

        # Letter in input string does not match last letter of wrapper.
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
            input_string, wrapper, idx_first_letter, idx_last_letter
        ):
            # Stop the search and return True if you find a scrambled substring.
            return True

    # If you reach this point then no permutations were found.
    return False


def check_for_substr_permutations(
    input_string: str, wrapper: StringWrapper, idx_first: int, idx_second: int
):
    """
    Check for substring permutations at the indices specified in search_indices.

    TODO: Update docstring.
    """
    logger.debug(
        "The middle of the input string is %s. Encoding as array.",
        input_string[idx_first + 1 : idx_second],
    )
    input_array = StringWrapper.str_to_array_encoding(
        input_string[idx_first + 1 : idx_second]
    )
    if int_arrays_equal(wrapper.mid_array_encoding, input_array):
        logger.debug("Permutation found between index %s and %s", idx_first, idx_second)
        return True


def int_arrays_equal(arr_1: list[int], arr_2: list[int]) -> bool:
    """Check if integer arrays arr_1 and arr_2 are equal."""
    for x, y in zip(arr_1, arr_2):
        if x != y:
            return False

    return True
