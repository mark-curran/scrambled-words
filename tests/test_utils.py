"""Tests for the utils.py module."""

from src.utils import (check_for_scrambled_substring,
                       check_for_substr_permutations, int_arrays_equal)


def test_int_arrays_equal():
    """Test the int_arrays_equal funciton."""

    assert int_arrays_equal([1, 2, 3], [1, 2, 3])
    assert not int_arrays_equal([1, 1, 1], [1, 3, 4])


def test_check_for_substr_permutations(axpaj_string_wrapper):
    """Test for check_for_substr_permutations."""
    # Test with an input stubstring that does have a scrambled substring.
    assert check_for_substr_permutations(
        input_string="aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt",
        wrapper=axpaj_string_wrapper,
        idx_first=0,
        idx_second=4,
    )
    # Test with an input stubstring that does not have a scrambled substring.
    assert not check_for_substr_permutations(
        input_string="nopermutationhere",
        wrapper=axpaj_string_wrapper,
        idx_first=0,
        idx_second=4,
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

def test_count_scrambled_substrings():
    # TODO: Finish writing this test.