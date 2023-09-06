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
    

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
            Implement my solution here
            
            Build a look-up array so that it can represent the number of item should be placed inside it
            Given the number of slot - k and the total items 
            
        
        May be we need 2 loops:
            - First loop to count the total items inside the single linked list and then build up the loop up table
            - Second loop, we just need to find the item that we need to "brake" the chain by list all head inside the returned list and break the chain
        """
        def divide(total: int, n: int) -> List[int]:
            """
                Try to divide total items into n slots, equal as much as possible and the left is bigger than the right
            """
            q, r = divmod(total, n)
            ans = [q] * n
            for i in range(r): 
                ans[i] += 1
            return ans         

        # Edge case, if the ListNode has length 0
        if head is None:
            return [None] * k
        
        # 1. Loop to the end of the ListNode and count the length
        length = 0 
        head_copy = head
        
        while head.next:
            length += 1
            head = head.next
            
        # Count for the last Node
        length += 1
        print(f'Length of the ListNode is: {length}')
        
        # 2. Use divide function to decide how many item should be contained inside each slot
        divided = divide(total=length, n=k)
        print(f'Divided: {divided}')
        
        # 3. Track the head of the start of ListNode
        rs = []
        pivot = head_copy
        for num in divided:
            rs.append(pivot)
            if pivot is None:
                continue
            for _ in range(num):
                print(f'Current pivot: {pivot.val}')
                # Loop through the head
                head_copy = pivot
                pivot = pivot.next
            print('====')
            
            if pivot is not None:
                print(f'Setting the head: {pivot.val}')
                print(f'Head copy: {head_copy.val}')
            head_copy.next = None

        return rs
            
def print_parts(lst: List[Optional[ListNode]]):
    """
    Loop to print all ListNode inside the lst
    """
    for index, list_node in enumerate(lst):
        print(f'==== Index: {index} ====')
        if list_node is None:
            print(f'Value: None')
            continue
        
        while list_node.next:
            print(f'Value: {list_node.val}')
            list_node = list_node.next
        print(f'Value: {list_node.val}')
    

def build_lookup(total, n):
    """
        Try to divide total items into n segments
    """
    q, r = divmod(total, n)
    rs = [q] * n
    for i in range(r): 
        rs[i] += 1
    print(f'Rs: {rs} with Sum: {sum(rs)}')
    pass

if __name__ == '__main__':
    # Prepare test case
    head_1 = ListNode(val=1, next=None)
    b = ListNode(val=2, next=None)
    c = ListNode(val=3, next=None)
    
    head_1.next = b
    b.next = c
    
    
    # Test case 2 
    head_2 = ListNode(val=1, next=None)
    d = ListNode(val=2, next=None)    
    e = ListNode(val=3, next=None)    
    f = ListNode(val=4, next=None)    
    g = ListNode(val=5, next=None)    
    h = ListNode(val=6, next=None)    
    j = ListNode(val=7, next=None)    
    k = ListNode(val=8, next=None)    
    l = ListNode(val=9, next=None)    
    m = ListNode(val=10, next=None)    

    head_2.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = j
    j.next = k
    k.next = l
    l.next = m
    
    # Test case 3
    head_3 = None
    
    # Number of nodes in the range [0, 1000]
    
    s = Solution()
    
    # Check the example is correct
    
    # print_parts(lst=[head_1])
    # print_parts(lst=[head_2])
    # print_parts(lst=[head_3])
    
    # res_1 = s.splitListToParts(head=head_1, k=5)
    # print_parts(lst=res_1)
    
    res_2 = s.splitListToParts(head=head_2, k=12)
    print_parts(lst=res_2)
    
    # res_3 = s.splitListToParts(head=head_3, k=10)
    # print_parts(lst=res_3)