"""
Description
___________
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
___________
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.

Approach
_____________
Since definition of a balanced binary tree depeneds upon
1. left balance ? 2. right balance? 3. abs (h_l - h_r) <= 1?
So divide and conquer and return
height of the tree, isBalanced or not

Complexity
___________
O(N)
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here

        def validate(root):

            if root is None:
                return True, 0

            left_balanced, left_height = validate(root.left)

            if not left_balanced:
                return False, 0

            right_balanced, right_height = validate(root.right)

            if not right_balanced:
                return False, 0

            return (abs(right_height - left_height) <= 1, max(left_height, right_height) + 1)

        result, _ = validate(root)
        return result