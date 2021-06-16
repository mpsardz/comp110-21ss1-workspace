"""Unit tests for list utils."""

import pytest
from lessons.ls27_list_utils import concat, max
# python -m pytest lessons/ls27_list_utils_test.py

def test_concat_edge_1() -> None:
    """Testing concat with a empty."""
    assert concat([], [2]) == [2]

def test_concat_edge_2() -> None:
    """Testing concat with b empty."""
    assert concat([4], []) == [4]

def test_concat_edge_3() -> None:
    """Testing concat with both empty."""
    assert concat([], []) == []

def test_concat_use_1() -> None:
    """Testing concat with aelt each."""
    assert concat([1], [2]) == [1, 2]

def test_max_edge_case() -> None:
    """Testing max wiht empty list."""
    with pytest.raises(ValueError):
        max([])

def test_max1() -> None:
    """Test max with a single element."""
    assert max([110]) == 110
    
def test_max2() -> None:
    """Test max with multi[le elements."""
    assert max([1, 5, 2]) == 5
    