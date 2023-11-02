""" 
    Problem statement:
        Given the root of a binary tree, return the number of nodes where the value of the node is equal to the 
        average of the values in its subtree.
        
        Note:
            * The average of n elements is the sum of the n elements divided by n and rounded down to the nearest 
            integer.
            
            * A subtree of root is a tree consisting of root and all of its descendants.

        Example 1:
            Input: root = [4,8,5,0,1,null,6]
            Output: 5
            Explanation: 
                For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
                For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
                For the node with value 0: The average of its subtree is 0 / 1 = 0.
                For the node with value 1: The average of its subtree is 1 / 1 = 1.
                For the node with value 6: The average of its subtree is 6 / 1 = 6.
                
        Example 2:
            Input: root = [1]
            Output: 1
            Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

        Constraints:
            * The number of nodes in the tree is in the range [1, 1000].
            * 0 <= Node.val <= 1000
            
        Hints:
            * What information do we need to calculate the average ? We need the sum of the values and the number of values.
            * Create a recursive function that return the size of a node's subtree, and the sum of the values of its subtree.
            
        Brain storming:
            * May be we can use DP, here the DP is the dictionary like: {id: (size_of_node_subtree, sum_of_its_subtre, original_val, parent_id)}
            * At each node, we need to take account for the size of node substree and the sum of the values of its subtree
            * For deterministic, assign each node with the specific ID
            * Performing Depth First Search, each time we found a new Leaf Node then perform the update for each dictionary
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree_Naive(self, root: Optional[TreeNode]) -> int:
        """
            Efficient in memory 
        """
        # Perform the Depth First Search 
        lookup_table = dict() # type: dict
        my_stack = deque()  # type: deque
        id = 0  # ID: 0 mean root, the stack now contains
        my_stack.append((root, id, -1))  # The last term refer to the parent_id of this node
        lookup_table.update({id: [1, root.val, root.val,-1]})
        
        while len(my_stack):
            curr_node, curr_node_id, parent_id = my_stack.pop()
            print(f'Val: {curr_node.val}, Node ID: {curr_node_id}, Parent ID: {parent_id}')
            
            left, right = curr_node.left, curr_node.right
            
            if right is not None:
                print(f'Found right node with val: {right.val}')
                id += 1
                my_stack.append((right, id, curr_node_id))
                
                # Update for this node 
                lookup_table.update({id: [1, right.val, right.val, curr_node_id]})
                
                # Update for all parents node's
                tmp = curr_node_id
                while tmp != -1:
                    p_node = lookup_table[tmp]
                    print(f'Update for Parent Node: {p_node}')
                    lookup_table[tmp] = [p_node[0] + 1, p_node[1] + right.val, p_node[2], p_node[3]]
                    tmp = p_node[3]
                
                print(f'After updated: {lookup_table}')
                
            if left is not None:
                print(f'Found left node with val: {left.val}')
                id += 1
                my_stack.append((left, id, curr_node_id))
                
                # Update for this node
                lookup_table.update({id: [1, left.val, left.val, curr_node_id]})
                
                # Update for all parents node's 
                tmp = curr_node_id
                while tmp != -1:
                    p_node = lookup_table[tmp]
                    print(f'Update for Parent Node: {p_node}')
                    lookup_table[tmp] = [p_node[0] + 1, p_node[1] + left.val, p_node[2], p_node[3]]
                    tmp = p_node[3]
                    
                print(f'After updated: {lookup_table}')
        
        print(f'Final table: {lookup_table}')
        
        rs = 0
        for value in lookup_table.values():
            if value[1] // value[0] == value[2]:
                rs += 1
                
        return rs
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(root):
            """
                Return (size_of_node_subtree, sum_of_its_subtre)
            """
            if not root: # This leaf is not existed
                return 0, 0
            l, nl = dfs(root.left)
            r, nr = dfs(root.right)

            if (l + r + root.val)//(nl + nr + 1) == root.val:
                self.count += 1
            
            return l + r + root.val, nl + nr + 1
        
        dfs(root)
        return self.count


if __name__ == '__main__':
    s = Solution()
    
    # 1. Construct example 1
    a = TreeNode(val=0)
    b = TreeNode(val=1)
    c = TreeNode(val=6)
    d = TreeNode(val=8, left=a, right=b)
    e = TreeNode(val=5, right=c)
    root_1 = TreeNode(val=4, left=d, right=e)
    
    # 2. Construct example 2
    root_2 = TreeNode(val=1)
    
    print(s.averageOfSubtree(root=root_1))
    print(s.averageOfSubtree(root=root_2))