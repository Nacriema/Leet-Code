
"""
Hint:
    * Notice that for any given time t, the number of flowers booming at time t is equal to the number of 
    flowers that have started blooming minus the number of flowers that have already stopped blooming
    * We can obtain these values efficently using binary search
    * We can store the starting times in sorted order, which then allows us to binary search to find how many flowers have started blooming for a given time t.
    * We do the same for the ending times to find how many flowers have stopped blooming at time t.
"""
from typing import List
import bisect


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers_start_increased = sorted(flowers, key=lambda flower: flower[0])
        start_increased = [x[0] for x in flowers_start_increased]

        flowers_end_increased = sorted(flowers, key=lambda flower: flower[1])
        end_increased = [x[1] for x in flowers_end_increased]
        print(f'Start time increased array: {start_increased}')
        print(f'End time increased array: {end_increased}')

        #  Efficently bisec search if we sort the people
        people_increased = sorted(people)
        print(f'People increased array: {people_increased}')

        rs = []
        for t in people:
            # Find index of t inside the start increased
            start_t = bisect.bisect_right(start_increased, t)
            # Find index of t inside the end increased
            end_t = bisect.bisect_left(end_increased, t)
            rs.append(start_t - end_t)
        return rs

if __name__ == '__main__':
    s = Solution()
    print(s.fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
    print(s.fullBloomFlowers(flowers = [[1,10],[3,3]], people = [3,3,2]))
    print(s.fullBloomFlowers(flowers = [[2,7],[3,7],[3, 5],[9,12],[4,13]], people = [1,3,7,11]))
