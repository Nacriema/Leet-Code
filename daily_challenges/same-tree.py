"""
    Problem statement:
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

        Example 1:
            Input: p = [1,2,3], q = [1,2,3]
            Output: true

        Example 2:
            Input: p = [1,2], q = [1,null,2]
            Output: false

        Example 3:
            Input: p = [1,2,1], q = [1,1,2]
            Output: false

        Constraints:
            * The number of nodes in both trees is in the range [0, 100].
            * -10^4 <= Node.val <= 10^4
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodes = [(p, q)]
        while len(nodes):
            a, b = nodes.pop()
            print(nodes)
            # Check if these 2 node are the same
            if (a is None and b is None):
                continue
            elif (a is None and b is not None) or (a is not None and b is None):
                return False
            else:
                if not (a.left is None != b.left is None) and not (a.right is None != b.right is None):
                    if a is not None and b is not None:
                        if a.val == b.val:
                            nodes.append((a.left, b.left))
                            nodes.append((a.right, b.right))
                        else:
                            return False
                    else:
                        return False
        return True 


if __name__ == '__main__':
    s = Solution()
    
    # Example 2
    a = TreeNode(val=2)
    root1 = TreeNode(left=a)
    
    b = TreeNode(val=2)
    root2 = TreeNode(right=b)
    
    # Example 1
    c = TreeNode(val=2)
    d = TreeNode(val=3)
    e = TreeNode(val=2)
    f = TreeNode(val=3)
    root3 = TreeNode(val=1, left=c, right=d)
    root4 = TreeNode(val=1, left=e, right=f)
    
    # Example 3:
    g = TreeNode(val=2)
    h = TreeNode(val=1)
    
    i = TreeNode(val=1)
    k = TreeNode(val=2)
    root5 = TreeNode(val=1, left=g, right=h)
    root6 = TreeNode(val=1, left=i, right=k)

    # print(s.isSameTree(root1, root2))
    # print(s.isSameTree(root3, root4))
    print(s.isSameTree(root5, root6))