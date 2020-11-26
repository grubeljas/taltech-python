"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Mul(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """priority of the operation."""
        return 2

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return False

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(self.actions[type(self.left.apply()), type(self.right.apply())], "*")

    @property
    def actions(self):
        """:return a dictionary of custom operations. Make use of frozensets."""
        return {
            (set, set): lambda x, y: {frozenset({a, b}) for a in x for b in y},  # cartesian product
            (set, int): lambda x, y: {frozenset({a, y}) for a in x},  # {1, 3} * 2 == {{1, 2}, {3, 2}}
            (int, set): lambda x, y: {frozenset({x, b}) for b in y},  # 2 * {1, 3} == {{2, 1}, {2, 3}}
            (int, int): lambda x, y: x * y
        }
