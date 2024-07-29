""" 
    Problem Statement:
        URL: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150
        530. Minimum Absolute Difference in BST
        Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

        Example 1:
            Input: root = [4,2,6,1,3]
            Output: 1

        Example 2:
            Input: root = [1,0,48,null,null,12,49]
            Output: 1

        Constraints:
            * The number of nodes in the tree is in the range [2, 10^4].
            * 0 <= Node.val <= 10^5

        Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
            Due to BST, use inoder traversal to get the sorted list
        """
        self.min_so_far = float('inf')
        self.prev_val = None
        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            if self.prev_val is not None:
                self.min_so_far = min(self.min_so_far, abs(self.prev_val - node.val))
            self.prev_val = node.val
            inorder_traversal(node.right)
        inorder_traversal(node=root)
        return self.min_so_far


if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(val=4)
    root1.left = TreeNode(val=2)
    root1.right = TreeNode(val=6)
    root1.left.left = TreeNode(val=1)
    root1.left.right = TreeNode(val=3)
    print(s.getMinimumDifference(root=root1))