"""Definition of the StringWrapper class."""

from string import ascii_lowercase

from configure_logging import getLogger

logger = getLogger(__name__)


class StringWrapper:
    """TODO: Class docstring."""

    def __init__(self, input_str: str) -> None:
        """Initiate the StringWrapper class."""
        if not isinstance(input_str, str):
            raise TypeError(
                f"StringWrapper can only wrap strings and {input_str} is not a string."
            )
        if len(input_str) == 1:
            raise ValueError(
                f"Input string {input_str} is not of length greater than 1."
            )

        # TODO: Rename input_str, this is very confusing in practice.
        self.input_str = input_str
        self._first_letter = input_str[0]
        self._last_letter = input_str[-1]
        self._length = len(input_str)
        self._mid_array_encoding = self.str_to_array_encoding(input_str[1:-1])

    @property
    def mid_array_encoding(self):
        """Get the byte array encoding of the input string."""
        return self._mid_array_encoding

    @mid_array_encoding.setter
    def mid_array_encoding_encoding(self):
        """Try to set the array_encoding attribute."""
        raise Exception("Cannot set the mid_array_encoding attribute.")

    @property
    def length(self):
        """Get the length of ths tring."""
        return self._length

    @length.setter
    def length(self):
        """Try to set the length attribute."""
        raise Exception("Cannot set the first length attribute.")

    @property
    def first_letter(self):
        """Get the first letter."""
        return self._first_letter

    @first_letter.setter
    def first_letter(self):
        """Try to set the first letter."""
        raise Exception("Cannot set the first letter attribute.")

    @property
    def last_letter(self):
        """Get the last letter."""
        return self._last_letter

    @last_letter.setter
    def last_letter(self):
        """Try to set the last letter."""
        raise Exception("Cannot set the last letter attribute.")

    @classmethod
    def str_to_array_encoding(cls, input_str: str):
        """Convert a string to a array encoding."""
        array = []
        for letter in ascii_lowercase:
            array.append(input_str.count(letter))

        return array


if __name__ == "__main__":
    # TODO: Delete this function.
    wrapper = StringWrapper("hello")

    breakpoint()
