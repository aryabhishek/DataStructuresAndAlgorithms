"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Link: https://leetcode.com/problems/sum-root-to-leaf-numbers
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.solve(root, 0)

    def solve(self, root, num):
        if not root:
            return 0

        if not root.left and not root.right:
            return num * 10 + root.val

        return self.solve(root.left, num * 10 + root.val) + self.solve(root.right, num * 10 + root.val)