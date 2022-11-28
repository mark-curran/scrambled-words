"""Definition of the StringWrapper class."""

from string import ascii_lowercase

from configure_logging import getLogger

logger = getLogger(__name__)


class StringWrapper:
    """Save some properties of a string.

    The mid_array_encoding is a sequence of 26 integers, each corresponding
    to the number of instances of that letter in that position in the alphabet
    that are present in the input string.
    """

    def __init__(self, base_str: str) -> None:
        """Wrap the base string.

        Args:
            base_str (str):
                Base string to be wrapped.

        Raises:
            TypeError: If base_str is not a string.
            ValueError: If base_str is not of length greater than 1.
        """
        if not isinstance(base_str, str):
            raise TypeError(
                f"StringWrapper can only wrap strings and {base_str} is not a string."
            )
        if len(base_str) == 1:
            raise ValueError(
                f"Input string {base_str} is not of length greater than 1."
            )

        self.base_str = base_str
        self._first_letter = base_str[0]
        self._last_letter = base_str[-1]
        self._length = len(base_str)
        self._mid_array_encoding = self.str_to_array_encoding(base_str[1:-1])
        logger.debug(
            "Mid array encoding of %s is: %s", self.base_str, self._mid_array_encoding
        )

    @property
    def mid_array_encoding(self):
        """Get the array encoding of the middle characters of the base string."""
        return self._mid_array_encoding

    @mid_array_encoding.setter
    def mid_array_encoding_encoding(self):
        """Try to set the array_encoding attribute."""
        raise Exception("Cannot set the mid_array_encoding attribute.")

    @property
    def length(self):
        """Get the length of the base string."""
        return self._length

    @length.setter
    def length(self):
        """Try to set the length attribute."""
        raise Exception("Cannot set the length attribute.")

    @property
    def first_letter(self):
        """Get the first letter of the base string."""
        return self._first_letter

    @first_letter.setter
    def first_letter(self):
        """Try to set the first letter."""
        raise Exception("Cannot set the first letter attribute.")

    @property
    def last_letter(self):
        """Get the last letter of the base string."""
        return self._last_letter

    @last_letter.setter
    def last_letter(self):
        """Try to set the last letter."""
        raise Exception("Cannot set the last letter attribute.")

    @classmethod
    def str_to_array_encoding(cls, base_str: str):
        """Convert a string to an array of 26 integers."""
        array = []
        for letter in ascii_lowercase:
            array.append(base_str.count(letter))

        return array
