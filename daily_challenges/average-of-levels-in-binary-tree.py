""" 
    Problem Statement:
        URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
        637. Average of Levels in Binary Tree
        Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

        Example 1:
            Input: root = [3,9,20,null,null,15,7]
            Output: [3.00000,14.50000,11.00000]
            Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
            Hence return [3, 14.5, 11].

        Example 2:
            Input: root = [3,9,20,15,7]
            Output: [3.00000,14.50000,11.00000]

        Constraints:
            * The number of nodes in the tree is in the range [1, 10^4].
            * -2^31 <= Node.val <= 2^31 - 1
"""
from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.level = defaultdict(list)
        def bfs(node, depth):
            if node is None:
                return
            print(f'Node: {node.val}, depth: {depth}')
            self.level[depth].append(node.val)
            bfs(node.left, depth+1)
            bfs(node.right, depth+1)
        bfs(node=root, depth=0)
        return [sum(v)/len(v) for k, v in self.level.items()]

if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(val=3)
    root1.left = TreeNode(val=9)
    root1.right = TreeNode(val=20)
    root1.right.left = TreeNode(val=15)
    root1.right.right = TreeNode(val=7)
    print(s.averageOfLevels(root=root1))
