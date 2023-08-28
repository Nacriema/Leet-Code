"""
    Problem Statement:
    
    - Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:

        - void push(int x) Pushes element x to the top of the stack.
        - int pop() Removes the element on the top of the stack and returns it.
        - int top() Returns the element on the top of the stack.
        - boolean empty() Returns true if the stack is empty, false otherwise.

    Notes:
        - You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
        - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""
from collections import deque

class MyStack:
    """
        Implement of a Stack using 2 Queues:
        NOTICE: 
            - Stack: LIFO
            - Queue: FIFO
            
        Approach: 
            - Implement the push operation more costly than others
            
        Init queue1, and queue2
        Implement the push(x) operation:
            - Enqueue x to queue2 (so that the x has the highest priority) ['x']
            - Dequeue items from queue1 and enqueue to queue2
            - Swap the queues between queue1 and queue2, queue1 is our like stack
    """
    def __init__(self) -> None:
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, x: int) -> None:
        # 1. Enqueue x to the queue2
        self.queue2.append(x)
        
        # 2. Dequeue items from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # 3. Swap queue
        self.queue1, self.queue2 = self.queue2, self.queue1
    
    def pop(self) -> int:
        return self.queue1.popleft()
    
    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        return None
    
    def empty(self) -> bool:
        return len(self.queue1) == 0
    
    
if __name__ == '__main__':
    obj = MyStack()
    print(obj.empty())
    obj.push(1)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
    
