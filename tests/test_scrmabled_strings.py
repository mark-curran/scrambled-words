"""Tests for the scrmabled_strings module."""
from src.scrmabled_strings import main


def test_main(capsys):
    """Test the main function."""
    main(
        dictionary_path="tests/data/test_dict.txt",
        input_path="tests/data/test_input.txt",
    )
    captured = capsys.readouterr()

    # NOTE: capsys append a new line character to captured strings, hence we
    # check for a string with two new line characters.
    assert captured.out == "Case: #1 4\nCase: #2 1\n\n"
