""" 
    Problem statement: 
        Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
        The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

        Example 1:
            Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
            Output: 2
            Explanation: 
                For arr1[0]=4 we have: 
                    |4-10|=6 > d=2 
                    |4-9|=5 > d=2 
                    |4-1|=3 > d=2 
                    |4-8|=4 > d=2 
                For arr1[1]=5 we have: 
                    |5-10|=5 > d=2 
                    |5-9|=4 > d=2 
                    |5-1|=4 > d=2 
                    |5-8|=3 > d=2
                For arr1[2]=8 we have:
                    |8-10|=2 <= d=2
                    |8-9|=1 <= d=2
                    |8-1|=7 > d=2
                    |8-8|=0 <= d=2

        Example 2:
            Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
            Output: 2

        Example 3:
            Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
            Output: 1

        Constraints:
            * 1 <= arr1.length, arr2.length <= 500
            * -1000 <= arr1[i], arr2[j] <= 1000
            * 0 <= d <= 100

        Hints:
            * Sort the arr2 and use binary search to get the closed element for each arr1[i], this will give the time complexity of O(nlogn)
"""
from typing import List
import bisect


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # 1. Sort the arr2
        arr2.sort()
        count = 0
        for item in arr1:
            low, hight = None, None
            # Find the closed value from arr2
            i = bisect.bisect_left(arr2, item)
            if i == len(arr2):
                hight = -1
                if abs(arr2[-1] - item) <= d:
                    continue
            elif i == 0:
                low = 0
                if abs(arr2[0] - item) <= d:
                    continue
            if low is None: low = i - 1
            if hight is None: hight = i
            if min(abs(arr2[hight] - item), abs(arr2[low] - item)) <= d:
                continue
            else:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))
    print(s.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3))
    print(s.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))