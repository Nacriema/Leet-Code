""" 
    Problem statement:
        Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
        For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
        Two binary trees are considered leaf-similar if their leaf value sequence is the same.
        Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

        Example 1:
            Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
            Output: true

        Example 2:
            Input: root1 = [1,2,3], root2 = [1,3,2]
            Output: false

        Constraints:
            * The number of nodes in each tree will be in the range [1, 200].
            * Both of the given trees will have values in the range [0, 200].
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            nonlocal ans
            if node:
                if node.left is None and node.right is None:
                    ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        ans = []   # type: list
        dfs(root1)
        leaf1 = ans.copy()
        ans = []
        dfs(root2)
        if leaf1 == ans:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    
    # Example 1
    a = TreeNode(val=6)
    b = TreeNode(val=7)
    c = TreeNode(val=4)
    d = TreeNode(val=9)
    e = TreeNode(val=8)
    
    f = TreeNode(val=2, left=b, right=c)
    g = TreeNode(val=5, left=a, right=f)
    h = TreeNode(val=1, left=d, right=e)
    
    root_1 = TreeNode(val=3, left=g, right=h)
    
    
    k = TreeNode(val=2, left=d, right=e)
    l = TreeNode(val=5, left=a, right=b)
    m = TreeNode(val=1, left=c, right=k)
    root_2 = TreeNode(val=3, left=l, right=m)

    print(s.leafSimilar(root1=root_1, root2=root_2))

    # Example 2
    
    # print(s.leafSimilar())