"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, function, mark):
        self.function = function
        self.mark = mark

    def __call__(self, left, right):
        return self.function(left, right)

    def __str__(self):
        return self.mark


if __name__ == '__main__':
    operator = DefaultOperator(lambda x, y: x + y, "+")
    assert operator.__call__(1, 2) == 3
    assert operator(1, 2) == 3
    assert operator.__str__() == "+"
    assert str(operator) == "+"
