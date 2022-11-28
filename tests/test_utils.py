"""Tests for the utils.py module."""

import pytest

from src.utils import (
    check_for_scrambled_substring,
    check_for_substr_permutations,
    count_scrambled_substrings,
    int_arrays_equal,
)


@pytest.fixture(name="list_input")
def fixture_list_input():
    """A list of strings to check."""

    return ["aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt"]


@pytest.fixture(name="dict_dict")
def fixture_dict_dict(dnrbt_string_wrapper, axpaj_string_wrapper):
    """A dictionary of wrappers of length 5."""

    return {5: [dnrbt_string_wrapper, axpaj_string_wrapper]}


def test_int_arrays_equal():
    """Test the int_arrays_equal funciton."""

    assert int_arrays_equal([1, 2, 3], [1, 2, 3])
    assert not int_arrays_equal([1, 1, 1], [1, 3, 4])


def test_check_for_substr_permutations(axpaj_string_wrapper):
    """Test for check_for_substr_permutations."""
    # Test with an input stubstring that does have a scrambled substring.
    input_str = "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt"

    assert check_for_substr_permutations(
        str_to_check=input_str[0 + 1 : 4], wrapper=axpaj_string_wrapper
    )
    # Test with an input stubstring that does not have a scrambled substring.
    assert not check_for_substr_permutations(
        str_to_check="nopermutationhere", wrapper=axpaj_string_wrapper
    )


def test_check_for_scrambled_substring(axpaj_string_wrapper):
    """Test for the check_for_scrambled_substring function."""
    # Test with an input stubstring that does have a scrambled substring.
    assert check_for_scrambled_substring(
        input_string="aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt",
        wrapper=axpaj_string_wrapper,
    )
    # Test with an input substring that does not contain the first letter.
    assert not check_for_scrambled_substring(
        input_string="helloworld",
        wrapper=axpaj_string_wrapper,
    )
    # Test with an input substring that contains the first letter, but the
    # second letter is invalid.
    assert not check_for_scrambled_substring(
        input_string="catdog",
        wrapper=axpaj_string_wrapper,
    )
    # Test with an input substring that contains the first letter, but the
    # position of the second letter is out of range.
    assert not check_for_scrambled_substring(
        input_string="bank",
        wrapper=axpaj_string_wrapper,
    )


def test_count_scrambled_substrings(dict_dict, list_input):
    """Test the count_scrambled_substrings function."""

    assert (
        count_scrambled_substrings(
            dict_dict, "aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt", [5]
        )
        == 2
    )
