""" 
    Problem statement:
        Given a binary tree where node values are digits from 1 to 9. 
        A path in the binary tree is said to be pseudo-palindromic if at least one permutation 
        of the node values in the path is a palindrome.

        Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
        
        Example 1:
            Input: root = [2,3,1,3,1,null,1]
            Output: 2 
            Explanation: The figure above represents the given binary tree. 
            There are three paths going from the root node to leaf nodes: the red path [2,3,3], 
            the green path [2,1,1], and the path [2,3,1].
            Among these paths only red path and green path are pseudo-palindromic paths since 
            the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] 
            can be rearranged in [1,2,1] (palindrome).

        Example 2:
            Input: root = [2,1,1,1,3,null,null,null,null,null,1]
            Output: 1 
            Explanation: The figure above represents the given binary tree. 
            There are three paths going from the root node to leaf nodes: the green path [2,1,1], 
            the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is 
            pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
        
        Example 3:
            Input: root = [9]
            Output: 1

        Constraints:
            * The number of nodes in the tree is in the range [1, 10^5].
            * 1 <= Node.val <= 9
"""
from typing import Optional
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            nonlocal ans
            if node:
                if node.left is None and node.right is None:
                    tmp = current.copy()
                    tmp[node.val] = current[node.val] + 1
                    ans.append(tmp)
                if node.left:
                    tmp = current.copy()
                    tmp[node.val] = current[node.val] + 1
                    dfs(node.left, tmp)
                if node.right:
                    tmp = current.copy()
                    tmp[node.val] = current[node.val] + 1
                    dfs(node.right, tmp)
        ans = []
        rs = 0
        dfs(root, {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
        for path in ans:
            even = 0
            for k, v in path.items():
                if v % 2 == 1:
                    even += 1
            if even <= 1:
                rs += 1 
        return rs


if __name__ == '__main__':
    s = Solution()
    
    # Example 1:
    a = TreeNode(val=3)
    b = TreeNode(val=1)
    c = TreeNode(val=1)
    d = TreeNode(val=3, left=a, right=b)
    e = TreeNode(val=1, right=c)
    root_1 = TreeNode(val=2, left=d, right=e)
    
    print(s.pseudoPalindromicPaths(root=root_1))
