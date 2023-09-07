"""
    Problem Statement:
        Given the head of a Singly Linked List and two integers left and right where left <= right
        Reverse the nodes of the list from position left to position right, and return the reversed list
        Position count 1-index
        
    Example 1: 
        Input: head = [1,2,3,4,5], left = 2, right = 4
        Output: [1,4,3,2,5]

    Example 2:
        Input: head = [5], left = 1, right = 1
        Output: [5]
        
    Constrains: 
        * The number of nodes in the list is n
        * 1 <= n <= 500 
        * -500 <= Node.val <= 500
        * 1 <= left <= right <= n
    
    Follow up: 
        Solve by just one pass
"""
"""
    Problem Statement:
        Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
        The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
        The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
        Return an array of the k parts.
        
    Example 1:
        Input: head = [1,2,3], k = 5
        Output: [[1],[2],[3],[],[]]
        Explanation:
        The first element output[0] has output[0].val = 1, output[0].next = null.
        The last element output[4] is null, but its string representation as a ListNode is [].
        
    Example 2:
        Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
        Output: [[1,2,3,4],[5,6,7],[8,9,10]]
        Explanation:
        The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self) -> str:
        return f'Node val: {self.val}'
    

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            My implementation here
            
            Idea for single loop
            1. Tracking correct index of the linked list firt. DONE
            2. Through the loop, keep track the "Pre-left" and the "Last-right" Node.
            
        """
        index = 1
        pre_left_node = head
        print(f'Init Pre-Left node: {pre_left_node}')
        last_right_node = None
        prev_head = None
        
        left_node = None  # Node at left index
        right_node = None # Node at right index
        
        head_cpy = head
        
        if head.next is None:
            return head
        
        while head.next:
            print(f'Index at {index} has value: {head.val}')
            
            # TODO: Tracking the previous pointer
            if index == left == right:
                pre_left_node = prev_head
                print(f'xxxx Change Pre-Left node to: {pre_left_node}')
                last_right_node = head.next
                left_node = right_node = head
            
            else:
                if index == left:
                    pre_left_node = prev_head
                    print(f'xxxx Change Pre-Left node to: {pre_left_node}')
                    left_node = head
                    
                elif index == right:
                    last_right_node = after_head
                    right_node = head
            
            if index in range(left, right + 1):
                # During the chain, remake the 
                print(f"Inside the chain current index: {index}, Previous head: {prev_head if prev_head is None else prev_head.val}")
                
                tmp = head.next
                tmp2 = head
                
                head.next = prev_head
                # prev_head.next = None
                print(f'[PROCESSED] Current: {head}, Next: {head.next}')
                
                head = tmp
                prev_head = tmp2
                after_head = head.next
                print(f'[NEXT] head: {head}, prev_head: {prev_head}, after_head: {after_head}')
            else:
                # Update node for the next loop
                prev_head =  head
                after_head = head.next.next
                head = head.next
            
            index += 1
        
        # TODO: Process for the last node
        if index == left == right:
            pre_left_node = prev_head
            print(f'xxxx Change Pre-Left node to: {pre_left_node}')

            last_right_node = head.next
            left_node = right_node = head
            
        else:
            if index == left:
                pre_left_node = prev_head
                print(f'xxxx Change Pre-Left node to: {pre_left_node}')

                left_node = head
                
            elif index == right:
                print(f"REACHED {index}")
                last_right_node = head.next
                right_node = head
                
        
                # During the chain, remake the 
                print(f"Inside the chain current index: {index}, Previous head: {prev_head if prev_head is None else prev_head.val}")
                
                tmp = head.next
                tmp2 = head
                
                head.next = prev_head
                # prev_head.next = None
                print(f'[PROCESSED] Current: {head}, Next: {head.next}')
                
                
                head = tmp
                prev_head = tmp2
                after_head = None
                print(f'[NEXT] head: {head}, prev_head: {prev_head}, after_head: {after_head}')
        
        
        print('=' * 20)
        print(f'Pre-Left node is: {pre_left_node}')
        print(f'Last-Right node is: {last_right_node}')
        
        if pre_left_node is not None:
            pre_left_node.next = right_node
            
        left_node.next = last_right_node
        
        if pre_left_node is not None:
            return head_cpy
        
        return right_node

def print_linked_list(header: Optional[ListNode]):
    """
    Loop to print all ListNode inside the lst
    """
    res = []
    count = 0
    while header.next:
        if count == 10:
            break
        res.append(str(header.val))
        header = header.next
        count += 1
    res.append(str(header.val))
    print(f'{" -> ".join(res)}')    


if __name__ == '__main__':
    # Prepare test cases
    
    # Test case 1
    # [1, 2, 3, 4, 5] left=1, right=4
    
    # head_1 = ListNode(val=1, next=None)
    # b = ListNode(val=2, next=None)
    # c = ListNode(val=3, next=None)
    # d = ListNode(val=4, next=None)
    # e = ListNode(val=5, next=None)
    
    # head_1.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    
    
    # Test case 2 
    # [5] left=1, right=1
    
    # head_2 = ListNode(val=5, next=None)
    
    
    # Test case 3
    head_3 = ListNode(val=1, next=None)
    b = ListNode(val=2, next=None)
    c = ListNode(val=3, next=None)
    d = ListNode(val=4, next=None)
    e = ListNode(val=5, next=None)
    f = ListNode(val=6, next=None)
    g = ListNode(val=7, next=None)
    h = ListNode(val=8, next=None)
    i = ListNode(val=9, next=None)
    
    head_3.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = i
    
    
    # Solution here
    s = Solution()
    
    print(f"Given list:")
    # print_linked_list(header=head_1)
    # print_linked_list(header=head_2)
    print_linked_list(header=head_3)
    
    # result_1 = s.reverseBetween(head=head_1, left=2, right=4)
    # result_2 = s.reverseBetween(head=head_2, left=1, right=1)
    result_3 = s.reverseBetween(head=head_3, left=8, right=9)

    print('===== Result =====')
    # print_linked_list(header=result_1)    
    # print_linked_list(header=result_2)
    print_linked_list(header=result_3)
    