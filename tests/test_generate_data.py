"""Tests for the generate_data.py module."""
from os.path import getmtime
from pathlib import Path

import pytest

from src.generate_data import make_dict_file, make_input_file


@pytest.mark.parametrize("num_entries,max_str_length", [(8, 20), (5, 15), (10, 15)])
def test_make_input_file(tmp_path: Path, num_entries: int, max_str_length: int):
    """Test the make_input_file function."""
    filepath = tmp_path / "test_input_file.txt"
    make_input_file(
        num_entries=num_entries, output_file=filepath, max_str_length=max_str_length
    )

    # Initiate a character and line counter for the temporary file.
    line_counter = 0

    with open(filepath, "r", encoding="utf-8") as file_contents:
        for line in file_contents:
            # Test every line ends in new line character.
            assert line[-1] == "\n"
            # Test each line is leq than the max_str_length.
            assert len(line[:-1]) <= max_str_length
            # Test all other characters are lowercase
            for char in line[:-1]:
                assert char.islower()

            # Increment the line counter.
            line_counter += 1

    # Test file has correct number of entries.
    assert line_counter == num_entries


@pytest.mark.parametrize(
    "num_entries,max_str_length,invalid_str_length",
    [(8, 70, 1), (5, 80, 200), (10, 90, 106)],
)
def test_make_dict_file(
    tmp_path: Path, num_entries: int, max_str_length: int, invalid_str_length: int
):
    """Test the make_dict_file function."""
    filepath = tmp_path / "test_dict_file.txt"
    make_dict_file(num_entries, filepath, max_str_length)

    # Save last modified time.
    lastmtime = getmtime(filepath)

    # Initiate a character and line counter for the temporary file.
    char_counter = 0
    line_counter = 0

    with open(filepath, "r", encoding="utf-8") as file_contents:
        for line in file_contents:
            # Test every line ends in new line character.
            assert line[-1] == "\n"
            # Test each line is leq than the max_str_length.
            assert len(line[:-1]) <= max_str_length
            # Test all other characters are lowercase
            for char in line[:-1]:
                assert char.islower()
                # Increment the character counter.
                char_counter += 1

            # Increment the line counter.
            line_counter += 1

    # Test we didn't exceed the line or character limits.
    assert line_counter <= num_entries
    assert char_counter <= 105

    # Test exception is raised if max_string_length is not between 2 and 105.
    with pytest.raises(
        ValueError,
        match=f"max_string_length {invalid_str_length} must be between 2 and 105 inclusive.",
    ):
        make_dict_file(num_entries, filepath, invalid_str_length)

    # Test the file was not modified during the last two tests.
    assert lastmtime == getmtime(filepath)
