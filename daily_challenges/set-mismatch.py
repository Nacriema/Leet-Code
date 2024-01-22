""" 
    Problem statement:
        You have a set of integers s, which originally contains all the numbers from 1 to n. 
        Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
        You are given an integer array nums representing the data status of this set after the error.
        Find the number that occurs twice and the number that is missing and return them in the form of an array.

        Example 1:
            Input: nums = [1,2,2,4]
            Output: [2,3]

        Example 2:
            Input: nums = [1,1]
            Output: [1,2]

        Constraints:
            * 2 <= nums.length <= 10^4
            * 1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        rs = [1, 1]  # Result
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                rs[0] = nums[i]
            prev = nums[i]
        rs[1] = set(range(1, len(nums) + 1)).difference(set(nums)).pop()
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums(nums=[1, 2, 2, 4]))
    print(s.findErrorNums(nums=[1, 1]))
    print(s.findErrorNums(nums=[1, 3, 2, 1]))  # Expect [1, 4] - 1, 1, 2, 3