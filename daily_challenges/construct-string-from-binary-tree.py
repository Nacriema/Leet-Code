"""
    Problem statement:  
        Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
        Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

        Example 1:
            Input: root = [1,2,3,4]
            Output: "1(2(4))(3)"
            Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"

        Example 2:
            Input: root = [1,2,3,null,4]
            Output: "1(2()(4))(3)"
            Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

        Constraints:
            * The number of nodes in the tree is in the range [1, 10^4].
            * -1000 <= Node.val <= 1000
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        string = str(root.val)
        
        # This is the preorder traversal !!!
        if root.left or root.right:
            string += f'({self.tree2str(root.left)})'
        if root.right:
            string += f'({self.tree2str(root.right)})'
        return string


if __name__ == '__main__':
    s = Solution()
    a = TreeNode(val=4)
    b = TreeNode(val=2, left=a)
    c = TreeNode(val=3)
    root_1 = TreeNode(val=1, left=b, right=c)  # "1(2(4)())(3()())" -> "1(2(4))(3)" 
    print(s.tree2str(root=root_1))
    
    d = TreeNode(val=4)
    e = TreeNode(val=2, right=d)
    f = TreeNode(val=3)
    root_2 = TreeNode(val=1, left=e, right=f)
    print(s.tree2str(root=root_2))  # "1(2()(4))(3)"