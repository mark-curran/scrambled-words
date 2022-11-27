"""Fixtures that are used across multiple tests."""
from unittest.mock import Mock

import pytest


@pytest.fixture(name="axpaj_string_wrapper")
def fixture_string_wrapper():
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
