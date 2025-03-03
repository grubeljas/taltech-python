"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Sub(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """priority of the operation."""
        return 4

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return True

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(self.actions[type(self.left.apply()), type(self.right.apply())], "-")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, int): lambda x, y: x - {y},  # set without the element
            (int, int): lambda x, y: x - y,
            (int, set): lambda x, y: {x} - y,
            (set, set): lambda x, y: x - y
        }
