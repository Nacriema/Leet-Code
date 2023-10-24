""" 
    Problem statement:
        Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed)
        
        Example 1:
            Input: root = [1,3,2,5,3,null,9]
            Output: [1,3,9]
            
        Example 2:
            Input: root = [1,2,3]
            Output: [1,3]
            
        Constraints:
            * The number of nodes in the tree will be in the range [0, 10^4]
            * -2^31 <= Node.val <= 2^31 -1
"""
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
            Use Breath First Search to search for all Node at the same level.
            Wwhen reaching all Nodes for the same level, then retreive the max value from them and then add to the final result
        """
        if root is None:
            return []
        rs = []
        top = deque()
        bottom  = deque()
        top.append(root)
        
        def BFS(top, bottom, rs):
            max_so_far = float('-inf')
            # 1. Do BFS, use Queue, and after reaching each level, then we do the reaching
            while len(top):
                cur = top.popleft()
                max_so_far = max(cur.val, max_so_far)
                # 2. Check the left and right node for this current Node
                if cur.left is not None:
                    bottom.append(cur.left)
                if cur.right is not None:
                    bottom.append(cur.right)
            rs.append(max_so_far)
        
        while len(top):
            BFS(top=top, bottom=bottom, rs=rs)
            # 3. At this point, we have all values of the bottom, switch the bottom with the top
            bottom, top = top, bottom
        
        return rs

if __name__ == '__main__':
    s = Solution()
    
    a = TreeNode(val=5, left=None, right=None)
    b = TreeNode(val=3, left=None, right=None)
    c = TreeNode(val=9, left=None, right=None)
    d = TreeNode(val=3, left=a, right=b)
    e = TreeNode(val=2, left=None, right=c)
    root_1 = TreeNode(val=1, left=d, right=e)
    print(s.largestValues(root=root_1))
    
    a = TreeNode(val=2, left=None, right=None)
    b = TreeNode(val=3, left=None, right=None)
    root_2 = TreeNode(val=1, left=a, right=b)
    print(s.largestValues(root=root_2))