""" 
    Problem statement:
        You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
        Return the minimum number of moves to make every value in nums unique.
        The test cases are generated so that the answer fits in a 32-bit integer.

        Example 1:
            Input: nums = [1,2,2]
            Output: 1
            Explanation: After 1 move, the array could be [1, 2, 3].

        Example 2:
            Input: nums = [3,2,1,2,1,7]
            Output: 6
            Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
            It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

        Constraints:
            * 1 <= nums.length <= 10^5
            * 0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()        
        rs = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                tmp = nums[i]
                nums[i] = prev + 1
                prev = nums[i]
                rs += abs(nums[i] - tmp)
            else:
                prev = nums[i]
        return rs


if __name__ == '__main__':
    s = Solution()
    # print(s.minIncrementForUnique(nums = [1, 0]))
    print(s.minIncrementForUnique(nums = [1,2,2]))
    # print(s.minIncrementForUnique(nums = [3,2,1,2,1,7]))