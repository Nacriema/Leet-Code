"""
    Problem Statement:
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.
        You must solve the problem without modifying the array nums and use only constant extra space.

    Example 1:
        Input: nums = [1, 3, 4, 2, 2]
        Output: 2

    Example 2:
        Input: nums = [3, 1, 3, 4, 2]
        Output: 3

    Constraints:
        * 1 <= n <= 10^5
        * nums.length == n + 1
        * 1 <= nums[i] <= n
        * All the integers in nums appear only once except for precisely on integer which appears two or more times.

    Follow up:
        * How can we prove that at least one duplicate number must exist in nums ? 
        * Can you solve the problem in linear runtime complexity - O(n) ?

    Idea: 
        This idea may not be the best - in term of memory, but it should give the answer in linear O(n)
            * Create a checker list has the same size as the input, consider value like [0, 1] where 0: not yet and 1: visited 
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        """
        check = [0] * (len(nums) + 1)
        for num in nums:
            if check[num] == 1:
                return num
            else:
                check[num] = 1


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate(nums=[1,3,4,2,2]))
    print(s.findDuplicate(nums=[3,1,3,4,2]))