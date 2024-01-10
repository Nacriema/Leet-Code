"""
    Problem statement:
        You are given the root of a binary tree with unique values, and an integer start.
        At minute 0, an infection starts from the node with value start.

        Each minute, a node becomes infected if:
            * The node is currently uninfected.
            * The node is adjacent to an infected node.

        Return the number of minutes needed for the entire tree to be infected.

        Example 1:
            Input: root = [1,5,3,null,4,10,6,9,2], start = 3
            Output: 4
            Explanation: 
                The following nodes are infected during:
                    - Minute 0: Node 3
                    - Minute 1: Nodes 1, 10 and 6
                    - Minute 2: Node 5
                    - Minute 3: Node 4
                    - Minute 4: Nodes 9 and 2
                It takes 4 minutes for the whole tree to be infected so we return 4.

        Example 2:
            Input: root = [1], start = 1
            Output: 0
            Explanation: At minute 0, the only node in the tree is infected so we return 0.

        Constraints:
            * The number of nodes in the tree is in the range [1, 10^5].
            * 1 <= Node.val <= 10^5
            Each node has a unique value.
            A node with a value of start exists in the tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            nonlocal ans, table
            if node:
                ans.append(node.val)
            if node.left is not None:
                # Parent - children: two ways relationship
                tmp = table.get(node.val, [])
                tmp.append(node.left.val)
                table[node.val] = tmp
                
                tmp = table.get(node.left.val, [])
                tmp.append(node.val)
                table[node.left.val] = tmp
                dfs(node.left)
            if node.right is not None:
                tmp = table.get(node.val, [])
                tmp.append(node.right.val)
                table[node.val] = tmp
                
                tmp = table.get(node.right.val, [])
                tmp.append(node.val)
                table[node.right.val] = tmp
                dfs(node.right)
        
        ans = list() # type: list
        table = dict() # type: dict
        queue = [start] # type: list
        dead = {start: True} # type: dict
        
        dfs(root)
        print(f'All nodes: {ans}')  
        print(f'Table: {table}')        
        
        count = 0
        while len(dead) != len(ans):
            print(f'Dead nodes: {dead}')            
            # Loop through all neighbor
            flag = False
            clone = queue.copy()
            queue = []
            for _ in clone:
                neightbors = table[_]
                for item in neightbors:
                    if item not in dead.keys():
                        queue.append(item)
                        dead[item] = True
                        flag = True
            if flag:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    
    # Example 1: 
    a = TreeNode(val=9)
    b = TreeNode(val=2)
    c = TreeNode(val=4, left=a, right=b)
    d = TreeNode(val=10)
    e = TreeNode(val=6)
    f = TreeNode(val=3, left=d, right=e)
    g = TreeNode(val=5, right=c)
    root_1 = TreeNode(val=1, left=g, right=f)
    print(s.amountOfTime(root=root_1, start=3))
    # print(s.amountOfTime())
    
    # Wrong answer with case: [1,2,null,3,null,4,null,5], start = 3
    # Case:
    a = TreeNode(val=5)
    b = TreeNode(val=4, right=a)
    c = TreeNode(val=3, left=b)
    d = TreeNode(val=2, left=c)
    root_2 = TreeNode(val=1, left=d)
    print(s.amountOfTime(root=root_2, start=3))