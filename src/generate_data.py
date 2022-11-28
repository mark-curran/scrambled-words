"""Script to generate either a sample dictionary or sample data."""
from random import randint
from string import ascii_lowercase

from configure_logging import getLogger

logger = getLogger(__name__)


def make_dict_file(
    max_num_entries: int, output_file: str, max_str_length: int = 105
) -> None:
    """Write a sample dictionary to a specified location.

    The total number of characters is limited to 105, otherwise entries have
    random lengths.

    Args:
        max_num_entries (int):
            Maximum number of entries in the dictionary.
        output_file (str):
            Full path where file will be written.
        max_str_length (int, optional):
            Maximum length of any entry in the dictionary. Defaults to 105.

    Raises:
        ValueError: If the max_str_length is not between 2 and 105 inclusive.
    """
    # Validate max_str_length
    if not 2 <= max_str_length <= 105:
        raise ValueError(
            f"max_string_length {max_str_length} must be between 2 and 105 inclusive."
        )

    # Initialize a counter of the current length of the dictionary.
    current_total_chars = 0

    with open(output_file, "w", encoding="utf-8") as file:
        for j in range(0, max_num_entries):
            length = randint(1, max_str_length)
            logger.debug("Length of %s-th word is %s", j, length)

            # Note that k is a dummy variable.
            # pyright: reportUnusedVariable=none
            letters = [ascii_lowercase[randint(0, 25)] for k in range(0, length)]

            word = "".join(letters)

            current_total_chars += len(word)
            if current_total_chars > 105:
                logger.warning("Dictionary length exceeds 105, breaking from loop.")
                break
            else:
                logger.debug("Writing %s-th word to file. j-th word is %s", j, word)
                file.write(f"{word}\n")


def make_input_file(num_entries: int, output_file: str, max_str_length: int) -> None:
    """
    Write a sample input file to a specified location.

    Entries have random lengths between 2 and the maximum string length.

    Args:
        num_entries (int):
            The number of entries in the file.
        output_file (str):
            Full path where file will be written.
        max_str_length (int):
            Maximum length of any single entry.
    """
    with open(output_file, "w", encoding="utf-8") as file:
        for j in range(0, num_entries):
            length = randint(2, max_str_length)
            logger.debug("Length of %s-th word is %s", j, length)

            # Note that k is a dummy variable.
            # pyright: reportUnusedVariable=none
            letters = [ascii_lowercase[randint(0, 25)] for k in range(0, length)]

            word = "".join(letters)
            logger.debug("Writing %s-th word to file. j-th word is %s", j, word)
            file.write(f"{word}\n")


if __name__ == "__main__":
    # If run as a script, generate files with the below specs.
    make_dict_file(max_num_entries=10, output_file="./dict_file.txt", max_str_length=10)
    make_input_file(num_entries=100, output_file="./input_file.txt", max_str_length=50)
