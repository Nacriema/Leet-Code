"""
    Problem Statement:
        
        There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
        There are n + 1 taps located at points [0, 1, ..., n] in the garden.
        Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
        Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

    Example 1:
        Input: n = 5, ranges = [3,4,1,1,0,0]
        Output: 1
        Explanation: 
            The tap at point 0 can cover the interval [-3,3]
            The tap at point 1 can cover the interval [-3,5]
            The tap at point 2 can cover the interval [1,3]
            The tap at point 3 can cover the interval [2,4]
            The tap at point 4 can cover the interval [4,4]
            The tap at point 5 can cover the interval [5,5]
            Opening Only the second tap will water the whole garden [0,5]

    Example 2:
        Input: n = 3, ranges = [0,0,0,0]
        Output: -1
        Explanation: Even if you activate all the four taps you cannot water the whole garden.
        
    Constrains:
        * 1 <= n <= 10^4
        * ranges.length == n + 1
        * 0 <= ranges[i] <= 100
"""
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
            Implementation here
            
            Humm, this problem again the may be Greedy or DP. 
            
            Maybe DP problem
        """
        # 1. Generate the range for taps and sort them by the left value
        tap_ranges = []
        for index, value in enumerate(ranges):
            tap_ranges.append((index - value, index + value))
        tap_ranges  = sorted(tap_ranges, key=lambda x: x[0])
        print(tap_ranges)
        # 2. Start with the initial value:
        pivot = tap_ranges[0]
        count = 1
        support = None
        max_end = -1
        
        for i in range(1, len(tap_ranges)):
            print(f'At index {i}, current value: {tap_ranges[i]}, pivot: {pivot}, count: {count}')

            start, end = tap_ranges[i]
            
            if pivot[1] >= n: return count
            
            # Handle edge case, when the interval not interleave
            if start > pivot[1]:
                print("Start greater than Pivot_1 !!!!")
                if support is None and pivot[1] < n:
                    return -1
                
                if support is not None:
                    count += 1
                    pivot = support
                    max_end = -1
                    print(f'Change pivot to: {support}')
            
            if start <= 0 and end >= pivot[1]:
                # Negative and positive better, not increase
                pivot = tap_ranges[i]
                continue
                
            if start <= pivot[1] and end <= pivot[1]:
                # Contains inside, so not use this case
                continue
            
            if start == pivot[0] and end >= pivot[1]:
                pivot = tap_ranges[i]
                continue
            
            else:
                # Remember the biggest value that we can have from the pivot to later
                """
                Pivot: (0, 6) and current (1, 7)
                
                From the pivot to later example: (0, 6) there are many ways that the later can happened
                
                Example: (1, 7), (1, 8), (2, 7), (3, 8)
                Just get and we count +1 for the greatest END value 
                """
                if pivot[0] <= start <= pivot[1]:
                    max_end = max(max_end, pivot[1], end)
                    
                    if max_end >= n:
                        return count + 1
                    else:
                        # How can I choose the appropriate the index 
                        if max_end != pivot[1] and max_end == end: 
                            support = tap_ranges[i]
                        continue
                
                # print(f'Inside the else')
                # pivot = tap_ranges[i]
                # count += 1
            
            # Handle later
            # if start
        if pivot[1] < n: return -1
        return count
    

if __name__ == '__main__':
    s = Solution()
    # print(s.minTaps(n = 5, ranges = [3,4,1,1,0,0]))
    # print(s.minTaps(n = 5, ranges = [3,2,1,1,0,0]))
    # print(s.minTaps(n = 5, ranges = [3,2,1,1,0,1]))
    
    # print(s.minTaps(n=9, ranges=[0,5,0,3,3,3,1,4,0,4])) # Expect 2
    # print(s.minTaps(n=7, ranges=[1,2,1,0,2,1,0,1]))  # Expect 3
    
    # print(s.minTaps(n=17, ranges=[0,3,3,2,2,4,2,1,5,1,0,1,2,3,0,3,1,1]))  # Expect 3
    print(s.minTaps(n=5, ranges=[3,0,1,1,0,0]))
    pass
