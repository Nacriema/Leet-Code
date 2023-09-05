"""
    Problem Statement:
        A linked list if length n is given such that each node contains an additional random pointer,
        which could point to any node in the list or null
        
        Construct a deepcopy of the list. The deep copy should consist of exactly n brand new nodes, where
        each new node has its value if uts cirresoinding original node. Both the next and random pointer of 
        the new nodes should point to new nodes in the copied list such that the pointers in the original list
        and copied list represent the same list state. None of the pointers in the new list should point to nodes
        in the original list.
        
        For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes
        x and y in the copied list, x.random --> y
        
        Return the head of the copied linked list.
        
        The lined list is represented in the input/output as a list of n nodes. Each node is represented as a pair of 
        [val, random_index] where:
            * val: an integer representing Node.val
            * radom_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null 
            if it does not point to any node
            
    Example 1:
        Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        
    Example 2:
        Input: head = [[1,1],[2,1]]
        Output: [[1,1],[2,1]]
        
    Example 3:
        Input: head = [[3,null],[3,0],[3,null]]
        Output: [[3,null],[3,0],[3,null]]
        
    Constrains:
        * 0 <= n <= 1000
        * -10^4 <= Node.val <= 10^4
        * Node.random is null or is pointing to some node in the linked list
"""
from typing import Optional

# Definition for a Node 
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            My idea: Use 3 loops -> O(n)
            
            - First loop construct all new clone Node, and a hash map {id - memory_id: index}
            - Second loop track the index and the 
            - Second loop loop from end to start 
        """
        table = {}
        new_nodes = []
        count = 0
        head_clone = head
        
        # Empty case
        if head is None:
            return None
        
        # 1. First loop
        while head.next is not None:
            table.update({id(head): count})
            
            # Init new Node
            new_nodes.append(Node(x=head.val, next=None, random=None))
            head = head.next
            count += 1
        
        # Update for last Node
        print(f'Sanity check for head next: {head.next}')
        table.update({id(head): count})
        new_nodes.append(Node(x=head.val, next=None, random=None))
        print(f'Hashing table: {table}')
        
        # 2. Update relationship for all Nodes in new_nodes
        for i in range(len(new_nodes) - 1):
            new_nodes[i].next = new_nodes[i + 1]
        
        # 3. Third loop, here, we have the cloned version of head, loop through it
        curr_index = 0
        while head_clone.next is not None:
            # Get the index from id from lookup table 
            random_node_index = table.get(id(head_clone.random))
            print(f'Index of random node: {random_node_index}')

            # Setting the relation
            if random_node_index is not None:
                new_nodes[curr_index].random = new_nodes[random_node_index]
            head_clone = head_clone.next
            curr_index += 1
        
        # Update for the last item
        random_node_index = table.get(id(head_clone.random))
        if random_node_index is not None:
                new_nodes[curr_index].random = new_nodes[random_node_index]
        
        # 3. Return the first item of the cloned list
        return new_nodes[0]
    

if __name__ == '__main__':
    # Init the graph
    e = Node(x=1, next=None, random=None)  # Leaf node
    d = Node(x=10, next=e, random=None)
    c = Node(x=11, next=d, random=None)
    b = Node(x=13, next=c, random=None)
    a = Node(x=7, next=b, random=None)
    
    # Init the random
    a.random = None
    b.random = a
    c.random = e
    d.random = c
    e.random = a
    
    s = Solution()
    # a_new = s.copyRandomList(head=a)
    a_new = s.copyRandomList(head=None)

    print(a_new.next)
    
    while a_new.next is not None:
        if a_new.random is not None:
            print(f"Val: {a_new.val}, Random val: {a_new.random.val}, Id: {id(a_new)}")
        else: 
            print(f"Val: {a_new.val}, Random val: None, Id: {id(a_new)}")
        
        a_new = a_new.next    
    
    if a_new.random is not None:
        print(f"Val: {a_new.val}, Random val: {a_new.random.val}, Id: {id(a_new)}")
    else: 
        print(f"Val: {a_new.val}, Random val: None, Id: {id(a_new)}")
