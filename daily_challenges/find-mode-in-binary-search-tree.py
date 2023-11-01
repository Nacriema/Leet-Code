""" 
    Problem statement:
        Given the root of a binary search tree (BST) with duplicates, return all mode(s) (i.e the
        most frequently occurence element) in it.
        
        If the tree has more than one mode, return them in any order.
        
        Assume a BST is defined as follows:
            * The left subtree of a node contains only nodes with keys less than or equal to the node's key
            * The right subtree of  a node contains only nodes with keys greater than or equal to the node's key
            * Both the left and right subtree must also be the binary searh trees
            
        Example 1: 
            Input: root = [1,null,2,2]
            Output: [2]
            
        Example 2:
            Input: root = [0]
            Output: [0]
            
        Constraints:    
            * The number of nodes in the tree is in the range [1, 10^4].
            * -10^5 <= Node.val <= 10^5
            
        Follow up: 
            Could you do that without using any extra space ? Assume that the implicit stack space incurred due to recursion 
        does not count)
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """ 
        """
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
            Naive solution
        """
        table = dict()
        stack = deque()
        stack.append(root)
        while len(stack):
            curr_node = stack.popleft()
            
            # Process for value of this node
            table[curr_node.val] = table.get(curr_node.val, 0) + 1
            
            left, right = curr_node.left, curr_node.right
            if left is not None:
                stack.append(left)
            if right is not None:
                stack.append(right)
        
        # Sort the table based on 
        max_value = max(table.values())
        max_items = [key for key, value in table.items() if value == max_value]       
        return max_items    
    
if __name__ == '__main__':
    s = Solution()
    
    # 1. First case 
    a = TreeNode(val=2, left=None, right=None)
    b = TreeNode(val=2, left=a, right=None)
    root_1 = TreeNode(val=1, left=None, right=b)
    
    # 2. Second case
    root_2 = TreeNode(val=0, left=None, right=None)
    
    print(s.findMode(root=root_1))
    print(s.findMode(root=root_2))