""" 
    Problem statement:
        Design a system that manages the reseration state of n seats that are numbered from 1 to n.
        
        Implement the SeatManager class: 
            * SeatManager(int n) Initialize a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
            * int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns it number.
            * void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
            
        Example 1:
            Input
                ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
                [[5], [], [], [2], [], [], [], [], [5]]
            Output
                [null, 1, 2, null, 2, 3, 4, 5, null]

            Explanation
                SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
                seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
                seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
                seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
                seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
                seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
                seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
                seatManager.reserve();    // The only available seat is seat 5, so return 5.
                seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
        
        Constraints:
            * 1 <= n <= 10^5
            * 1 <= seatNumber <= n
            * For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
            * For each call to unreserve, it is guaranteed that seatNumber will be reserved.
            * At most 10^5 calls in total will be made to reserve and unreserve.
        
        Hints:
            * You need a data structure that maintains the states of the seats. This data structure should also allow you to get the first available seat and flip the state of a seat in a reasonable time.
            * You can let the data structure contains the available seats. Then you want to be able to get the lowest element and erase an element, in a resonable time.
            * Ordered sets support these operations.
"""
class SeatManagerTLE:
    def __init__(self, n: int):
        """ 
            Use set to manipulate the empty seat
        """
        self.available_seat = set(range(1, n+1))
        self.occupied_seat = set() # type: set
    
    def reserve(self) -> int:
        """
            Get the lowest available seat
            Set it to the occupied_seat
        """
        available = min(self.available_seat)  # Use some thing like min-heap instead of use the min method
        self.available_seat.remove(available)
        self.occupied_seat.add(available)
        return available
    
    def unreserve(self, seatNumber: int) -> None:
        self.occupied_seat.discard(seatNumber)
        self.available_seat.add(seatNumber)
    

from heapq import heapify, heappop, heappush

class SeatManager:
    def __init__(self, n: int):
        """ 
            Just use the minheap to maintain the mimimum available seat
        """
        self.available_seat = list(range(1, n+1))
        heapify(self.available_seat)
        self.occupied_seat = set() # type: set
    
    def reserve(self) -> int:
        """
            Get the lowest available seat
            Set it to the occupied_seat
        """
        available = heappop(self.available_seat)
        self.occupied_seat.add(available)
        return available
    
    def unreserve(self, seatNumber: int) -> None:
        self.occupied_seat.discard(seatNumber)
        heappush(self.available_seat, seatNumber)
    
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

if __name__ == '__main__':
    obj = SeatManager(n=5)
    print(obj.reserve())
    print(obj.reserve())
    obj.unreserve(seatNumber=2)
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    print(obj.reserve())
    obj.unreserve(seatNumber=5)
    pass