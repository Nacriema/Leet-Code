""" 
    Problem statement:
        Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

        Example 1:
            Input: arr = [1,2,2,6,6,6,6,7,10]
            Output: 6

        Example 2:
            Input: arr = [1,1]
            Output: 1

        Constraints:
            * 1 <= arr.length <= 10^4
            * 0 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """ 
            Use Booyer-Moore Algorithm
        """
        candidate = -1
        vote = 0
        for num in arr:
            if vote == 0:
                candidate = num
                vote = 1
            else:
                if num == candidate:
                    vote += 1
                    if vote > int(25 * len(arr) / 100):
                        return candidate 
                else:
                    vote = 1
                    candidate = num
        return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
    print(s.findSpecialInteger(arr = [1, 1]))
    print(s.findSpecialInteger(arr = [1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))
    print(s.findSpecialInteger(arr = [1,1,2,2,3,3,3,3]))
    print(s.findSpecialInteger(arr = [15,15,21,21,32,32,33,33,33,34,35]))
