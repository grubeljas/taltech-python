"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Div(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """priority of the operation."""
        return 3

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return True

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(lambda x, y: x / y, "/")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, set): {},  # set exclusion
            (set, int): {},  # remove from set
            (int, int): -1  # integer division
        }
