"""
    Problem statement:
        Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
        A good subarray is a subarray where:
            * Its length is at least two, and
            * The sum of the elements of the subarray is a multiple of k.
            
            Note that:
                * A subarray is a contiguous part of the array.
                * An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

        Example 1:
            Input: nums = [23,2,4,6,7], k = 6
            Output: true
            Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

        Example 2:
            Input: nums = [23,2,6,4,7], k = 6
            Output: true
            Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
            42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

        Example 3:
            Input: nums = [23,2,6,4,7], k = 13
            Output: false

        Constraints:
            * 1 <= nums.length <= 10^5
            * 0 <= nums[i] <= 10^9
            * 0 <= sum(nums[i]) <= 2^31 - 1
            * 1 <= k <= 2^31 - 1
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """ 
            Calculate cumulative sum 
            Divide them to get the remainder
            2 remainder same kind at least >= 2 index will be represent for the sum divided by k
        """
        table = {}
        # Cumulative sum 
        tmp = nums[0] = nums[0] % k
        table.update({tmp: 0})
        for i in range(1, len(nums)):
            tmp += nums[i]
            nums[i] = tmp % k
            if nums[i] == 0:
                return True
            check_idx = table.get(nums[i], -1)
            if check_idx != -1 and i - check_idx >= 2:
                return True
            if check_idx == -1:
                table.update({nums[i]: i})
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.checkSubarraySum(nums = [23, 2, 4, 6, 7], k = 6))   # [23, 25, 29, 35, 42]  True
    # print(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13))  # False 
    
    # print(s.checkSubarraySum(nums = [0], k = 1))
    # print(s.checkSubarraySum(nums = [1,0,1,0,1], k = 4))  # False
    # print(s.checkSubarraySum(nums = [0, 1, 0, 3, 0, 4, 0, 4, 0], k = 5))
    # print(s.checkSubarraySum(nums = [1, 2, 3], k = 5))
    # print(s.checkSubarraySum(nums = [1, 0], k = 2))
    # print(s.checkSubarraySum(nums= [1, 3, 6, 0, 9, 6, 9], k = 7))
    # print(s.checkSubarraySum(nums=[23,2,4,6,6], k=7))

    print(s.checkSubarraySum(nums = [5,0,0,0], k = 3))  # True 


    # [1, 2] -> [1, 3] -> [1, 1]
    # [1, 0] -> [1, 1] -> 