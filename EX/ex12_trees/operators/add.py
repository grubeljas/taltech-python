"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode
from operators.leaf import Leaf
from operators.sub import Sub


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
        return DefaultOperator(lambda x, y: x + y, "+")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (set, set): {},  # set union
            (set, int): {}  # add to set
        }


tree = Add(Sub(Leaf(5), Leaf(6)), Sub(Leaf(5), Leaf(6)))
print(tree)