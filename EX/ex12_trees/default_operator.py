"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, equation, mark):
        """."""
        self.equation = equation
        self.mark = mark

    def __call__(self, *args):
        """."""
        return self.equation(args[0], args[1])

    def __str__(self):
        """."""
        return self.mark


if __name__ == '__main__':
    operator = DefaultOperator(lambda x, y: x + y, "+")
    assert operator.__call__(1, 2) == 3
    assert operator(1, 2) == 3
    assert operator.__str__() == "+"
    assert str(operator) == "+"
    print(type(operator).__name__)
