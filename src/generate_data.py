"""Script to generate either a dictionary or sample data."""
from random import randint
from string import ascii_lowercase

from configure_logging import getLogger

logger = getLogger(__name__)


def make_dict_file(
    num_entries: int, output_file: str, max_str_length: int = 105
) -> str:
    """TODO: Write docstring."""
    # Validate max_str_length
    if not 2 <= max_str_length <= 105:
        raise ValueError(
            f"max_string_length {max_str_length} must be between 2 and 105 inclusive."
        )

    # Initialize a counter of the current length of the dictionary.
    current_total_chars = 0

    with open(output_file, "w", encoding="utf-8") as file:
        for j in range(0, num_entries):
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


def make_input_file(num_entries: int, output_file: str, max_str_length: int):
    """TODO: Write docstring."""

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
    make_dict_file(num_entries=10, output_file="./dict_file.txt", max_str_length=10)
    make_input_file(num_entries=100, output_file="./input_file.txt", max_str_length=50)
