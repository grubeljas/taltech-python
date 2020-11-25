"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Add(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))
        self.left = left
        self.right = right

    @property
    def priority(self):
        """:return the value of the operation."""
        return 4

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return False

    @property
    def default_operator(self):
        """:return the default operator of the operation."""
        return DefaultOperator(self.actions[type(self.left.apply()), type(self.right.apply())], "+")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (int, int): lambda x, y: x + y,
            (set, set): lambda x, y: x | y,  # set union
            (set, int): lambda x, y: x | {y},  # add to set
            (int, set): lambda x, y: {y} | x
        }
