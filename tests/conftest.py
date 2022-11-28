"""Fixtures that are used across multiple tests."""
from unittest.mock import Mock

import pytest

PATH_TEST_DICT = "tests/data/test_dict.txt"
PATH_TEST_INPUT = "tests/data/test_input.txt"


@pytest.fixture(name="dnrbt_string_wrapper")
def fixture_dnrbt_wrapper():
    """Mock wrapper for the string dnrbt."""
    mock_wrapper = Mock()
    mock_wrapper.base_str = "dnrbt_string_wrapper"
    mock_wrapper.mid_array_encoding = [
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    mock_wrapper.first_letter = "d"
    mock_wrapper.last_letter = "t"
    mock_wrapper.length = 5

    return mock_wrapper


@pytest.fixture(name="axpaj_string_wrapper")
def fixture_axpaj_wrapper():
    """Mock wrapper for the string axpaj."""
    mock_wrapper = Mock()
    mock_wrapper.base_str = "axpaj"
    mock_wrapper.mid_array_encoding = [
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
    ]
    mock_wrapper.first_letter = "a"
    mock_wrapper.last_letter = "j"
    mock_wrapper.length = 5

    return mock_wrapper
