"""."""

import pytest

from operators.leaf import Leaf
from operators.add import Add
from operators.sub import Sub
from operators.pow import Pow
from operators.or_ import Or
from operators.and_ import And
from operators.div import Div
from operators.mul import Mul


@pytest.mark.timeout(1.0)
def test_leaf_apply_yields_number_when_given_a_number():
    """."""
    assert Leaf(6).apply() == 6


@pytest.mark.timeout(1.0)
def test_addition_adds_when_given_leaves_with_numbers():
    """."""
    assert Add(Leaf(5), Leaf(6)).apply() == 11
    assert Add(Sub(Leaf(5), Leaf(6)), Sub(Leaf(5), Leaf(6))).__str__() == "5 - 6 + 5 - 6"
    assert Or(And(Leaf(3), Leaf(1)), And(Div(Mul(Pow(Leaf(5), Leaf(2)), Leaf(1)), Leaf(5)), Leaf(2))).__str__() == "3 & 1 | 5 ** 2 * 1 / 5 & 2"


@pytest.mark.timeout(1.0)
def test_subtract_subtracts_when_given_leaves_with_numbers():
    """."""
    assert Sub(Leaf(5), Leaf(6)).apply() == -1
    assert Leaf(5).__str__() == '5'
