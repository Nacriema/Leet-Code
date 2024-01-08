""" 
    Problem statement:
        Given the root node of a binary search tree and two integers low and high, 
        return the sum of values of all nodes with a value in the inclusive range [low, high].

    Example 1:
        Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
        Output: 32
        Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

    Example 2:
        Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
        Output: 23
        Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

    Constraints:
        *   The number of nodes in the tree is in the range [1, 2 * 104].
        *   1 <= Node.val <= 10^5
        *   1 <= low <= high <= 10^5
        *   All Node.val are unique.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


class Solution:
    def rangeSumBST_SLOW(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        rs =0
        while len(queue):
            current = queue.pop()
            if low <= current.val <= high:
                rs += current.val
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            if current.val < low and current.right and low <= current.right.val:
                queue.append(current.right)
            elif current.val > high and current.left and current.left.val <= high:
                queue.append(current.left)
        return rs

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ans
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        ans = 0
        dfs(root)
        return ans

if __name__ == '__main__':
    s = Solution()
    
    # Example 1:
    a = TreeNode(val=3)
    b = TreeNode(val=7)
    c = TreeNode(val=18)
    d = TreeNode(val=5, left=a, right=b)
    e = TreeNode(val=15, right=c)
    root_1 = TreeNode(val=10, left=d, right=e)
    print(s.rangeSumBST(root=root_1, low=7, high=15))
    
    # Example 2:
    a = TreeNode(val=1)
    b = TreeNode(val=6)
    c = TreeNode(val=3, left=a)
    d = TreeNode(val=7, left=b)
    e = TreeNode(val=13)
    f = TreeNode(val=18)
    g = TreeNode(val=5, left=c, right=d)
    h = TreeNode(val=15, left=e, right=f)
    root_2 = TreeNode(val=10, left=g, right=h)
    print(s.rangeSumBST(root=root_2, low=6, high=10))
