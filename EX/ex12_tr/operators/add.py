"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Add(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """:return the value of the operation."""
        return 0

    @property
    def default_operator(self):
        """:return the default operator of the operation."""
        return DefaultOperator(lambda x, y: x + y, "+")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, set): {},  # set union
            (set, int): {}  # add to set
        }
