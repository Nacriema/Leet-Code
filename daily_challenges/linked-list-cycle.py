"""
    Problem Statement:
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        There is a cycle in a linked list if there is some node in the list that can be reached again
        by coninuously following the next pointer. Internally, pos is used to denote the index of the node that
        tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Return True if there is a cycle in the linked list. Otherwise, return False

    Example 1:
        Input: head = [3, 2, 0, -4], pos = 1
        Output: True
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0 - indexes)    
    
    Example 2:
        Input: head = [1, 2], pos = 0
        Output: True
        Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

    Example 3: 
        Input: head = [0], pos = -1
        Output: False
        Explanation: There is no cycle in the linked list

    Constrains: 
        * The number of the nodes in the list is in the range [0, 10^4]
        * -10^5 <= Node.val <= 10^5
        * pos is -1 or a valid index in the linked-list

    Use Floyd's Cycle-Finding Algorithm
        - Fast pointer (2 steps) and Slow pointer (1 step)

    """
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while (slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

if __name__ == '__main__':
    # 1. Define the graph
    # Example 1: 
    ex_1 = ListNode(x=3)
    b = ListNode(x=2)
    c = ListNode(x=0)
    d = ListNode(x=-4)
    ex_1.next = b
    ex_1.next.next = c 
    ex_1.next.next.next = d 
    ex_1.next.next.next.next = b

    s = Solution()
    print(s.hasCycle(head=ex_1))