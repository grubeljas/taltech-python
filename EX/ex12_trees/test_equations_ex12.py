"""."""

import pytest

from operators.leaf import Leaf
from operators.add import Add
from operators.sub import Sub


@pytest.mark.timeout(1.0)
def test_leaf_apply_yields_number_when_given_a_number():
    """."""
    assert Leaf(6).apply() == 6


@pytest.mark.timeout(1.0)
def test_addition_adds_when_given_leaves_with_numbers():
    """."""
    assert Add(Leaf(5), Leaf(6)).apply() == 11
    assert Add(Sub(Leaf(5), Leaf(6)), Sub(Leaf(5), Leaf(6))).__str__() == "5 - 6 + 5 - 6"


@pytest.mark.timeout(1.0)
def test_subtract_subtracts_when_given_leaves_with_numbers():
    """."""
    assert Sub(Leaf(5), Leaf(6)).apply() == -1
    assert Leaf(5).__str__() == '5'
