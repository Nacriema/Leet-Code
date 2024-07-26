""" 
    Problem Statement:
        URL: https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150
        222. Count Complete Tree Nodes

        Given the root of a complete binary tree, return the number of the nodes in the tree.
        According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
        Design an algorithm that runs in less than O(n) time complexity.

        Example 1:
            Input: root = [1,2,3,4,5,6]
            Output: 6

        Example 2: 
            Input: root = []
            Output: 0

        Example 3:
            Input: root = [1]
            Output: 1

        Constraints:
            * The number of nodes in the tree is in the range [0, 5 * 10^4].
            * 0 <= Node.val <= 5 * 10^4
            * The tree is guaranteed to be complete.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """ 
            O(n) time complexity
        """
        self.count = 0
        def inorder_traversal(node):
            if node is None:
                return 
            inorder_traversal(node.left)
            self.count += 1
            inorder_traversal(node.right)
        inorder_traversal(node=root)
        return self.count


if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(val=1)
    root1.left = TreeNode(val=2)
    root1.right = TreeNode(val=3)
    root1.left.left = TreeNode(val=4)
    root1.left.right = TreeNode(val=5)
    root1.right.left = TreeNode(val=6)
    print(s.countNodes(root=root1))
