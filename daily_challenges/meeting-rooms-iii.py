""" 
    Problem statement:
        You are given an integer n. There are n rooms numbered from 0 to n - 1.
        You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a 
        meeting will be held during the half-closed time interval [starti, endi).
        All the values of starti are unique.
        Meetings are allocated to rooms in the following manner:
            1. Each meeting will take place in the unused room with the lowest number.
            2. If there are no available rooms, the meeting will be delayed until a room becomes free. 
            The delayed meeting should have the same duration as the original meeting.
            3. When a room becomes unused, meetings that have an earlier original start time should be 
            given the room.

        Return the number of the room that held the most meetings. If there are multiple rooms, 
        return the room with the lowest number.
        A half-closed interval [a, b) is the interval between a and b including a and not including b.

        Example 1:
        Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
        Output: 0
            Explanation:
            - At time 0, both rooms are not being used. The first meeting starts in room 0.
            - At time 1, only room 1 is not being used. The second meeting starts in room 1.
            - At time 2, both rooms are being used. The third meeting is delayed.
            - At time 3, both rooms are being used. The fourth meeting is delayed.
            - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
            - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
            Both rooms 0 and 1 held 2 meetings, so we return 0. 

        Example 2:
        Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
        Output: 1
        Explanation:
            - At time 1, all three rooms are not being used. The first meeting starts in room 0.
            - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
            - At time 3, only room 2 is not being used. The third meeting starts in room 2.
            - At time 4, all three rooms are being used. The fourth meeting is delayed.
            - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
            - At time 6, all three rooms are being used. The fifth meeting is delayed.
            - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
            Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 

        Constraints:
            * 1 <= n <= 100
            * 1 <= meetings.length <= 10^5
            * meetings[i].length == 2
            * 0 <= starti < endi <= 5 * 10^5
            * All the values of starti are unique.

        Hints:
            * Sort meetings based on start times
            * Use two min heaps, the first one keeps track of the numbers of all the rooms that are free. 
            The second heap keeps track of the end times of all the meetings that are happening and the 
            room that they are in.
            * Keep track of the number of times each room is used in an array.
            * With each meeting, check if there are any free rooms. If there are, then use the room with the smallest number.
            Otherwise, assign the meeting to the room whose meeting will end the soonest.
"""
from typing import List
import heapq

class Solution:
    def mostBooked_oneheap(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [[0, i] for i in range(n)]
        ans = [0] * n
        meetings.sort(key=lambda x: [x[0], x[1]])
        for curr_start, curr_end in meetings:
            while len(rooms) and rooms[0][0] < curr_start:
                _, prev_room = heapq.heappop(rooms)
                heapq.heappush(rooms, [curr_start, prev_room])
            prev_end, prev_room = heapq.heappop(rooms)
            heapq.heappush(rooms, [prev_end + (curr_end - curr_start), prev_room])
            ans[prev_room] += 1
        return ans.index(max(ans))

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1. Sort the meetings based on start times
        meetings.sort(key=lambda x: x[0])
        # 2. Use two min heap, first use to keep track the numbers of all rooms that are free
        # The second heap keeps track of the used room and the time that they ended 
        free_rooms = [[i, 0] for i in range(n)]
        occupied = []

        # 3. Keep track of the number of times each room is used in an array
        used = [0] * n
        for start, end in meetings:
            print(f'Got meeting start:{start}, end: {end}')
            print(f'Free rooms: {free_rooms}')
            print(f'Occupied: {occupied}')
            while len(occupied) and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(free_rooms, [room, 0])
            # Get the available room
            if len(free_rooms):
                room, prev_end = heapq.heappop(free_rooms)  # Get the smallest available room
                heapq.heappush(occupied, [prev_end + end, room])
                used[room] += 1
            else: # No room available now
                # Let's use the most finished room from occupied heap
                print('No room available now, get the room with least end time')
                end_time, room = heapq.heappop(occupied)
                print(f'Got room: {room} with end_time: {end_time}')
                # Put the delayed meeting to the occupied
                heapq.heappush(occupied, [end_time + (end - start), room])
                used[room] += 1
            print('===================')
        return used.index(max(used))


if __name__ == '__main__':
    s = Solution()
    # print(s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
    # print(s.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))
    # print(s.mostBooked(n = 2, meetings=[[0,10],[1,2],[12,14],[13,15]]))
    print(s.mostBooked(n = 4, meetings=[[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]]))