""" 
    Problem Statement:
        URL: https://leetcode.com/problems/delete-nodes-and-return-forest/description/?envType=daily-question&envId=2024-07-17
        1110. Delete Nodes And Return Forest

        Given the root of a binary tree, each node in the tree has a distinct value.
        After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
        Return the roots of the trees in the remaining forest. You may return the result in any order.

        Example 1:
            Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
            Output: [[1,2,null,4],[6],[7]]

        Example 2:
            Input: root = [1,2,4,null,3], to_delete = [3]
            Output: [[1,2,4]]

        Constraints:
            * The number of nodes in the given tree is at most 1000.
            * Each node has a distinct value between 1 and 1000.
            * to_delete.length <= 1000
            * to_delete contains distinct values between 1 and 1000.
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """ 
            Traverse through the tree
                - If the current node meet the condition in to_delete:
                    + Store the leftNode and rightNode, because they are the new root (if left and right not in the to_delete list)
                    + Break the node 
        """
        self.new_roots = []
        self.delete_nodes = []
        def dfs(node, parent_node, branch):
            if node:
                print(f'Visit {node.val}')
                # If we found the to_delete node
                if node.val in to_delete:
                    print(f'Found: {node.val}')
                    if node.left and node.left.val not in to_delete:
                        self.new_roots.append(node.left)
                        print(f'New root: {node.left.val}')
                    if node.right and node.right.val not in to_delete:
                        self.new_roots.append(node.right)
                        print(f'New root: {node.right.val}')
                    self.delete_nodes.append((parent_node, branch))
                dfs(node.left, node, branch='L')
                dfs(node.right, node, branch='R')
        if root.val not in to_delete:
            self.new_roots.append(root)
        dfs(root, parent_node=None, branch='')
        for node, branch in self.delete_nodes:
            # print(f'Node: {node.val}, Branch: {branch}')
            if node is not None:
                if branch == 'L':
                    node.left = None
                else:
                    node.right = None
        return self.new_roots


if __name__ == '__main__':
    s = Solution()

    # a = TreeNode(val=4)
    # b = TreeNode(val=5)
    # c = TreeNode(val=6)
    # d = TreeNode(val=7)
    # e = TreeNode(val=2, left=a, right=b)
    # f = TreeNode(val=3, left=c, right=d)
    # root1 = TreeNode(val=1, left=e, right=f)
    # print(s.delNodes(root=root1, to_delete=[3, 5]))

    a = TreeNode(val=4)
    b = TreeNode(val=3, right=a)
    c = TreeNode(val=2)
    root2 = TreeNode(val=1, left=c, right=b)
    print(s.delNodes(root2, [2, 1]))