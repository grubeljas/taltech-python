"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    pass


if __name__ == '__main__':
    operator = DefaultOperator(lambda x, y: x + y, "+")
    assert operator.__call__(1, 2) == 3
    assert operator(1, 2) == 3
    assert operator.__str__() == "+"
    assert str(operator) == "+"
