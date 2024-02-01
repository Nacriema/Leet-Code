""" 
    Problem statement:
        You are given an integer array nums of size n and a positive integer k.
        Divide the array into one or more arrays of size 3 satisfying the following conditions:

            * Each element of nums should be in exactly one array.
            * The difference between any two elements in one array is less than or equal to k.

        Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, 
        return an empty array. And if there are multiple answers, return any of them.

        Example 1:
            Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
            Output: [[1,1,3],[3,4,5],[7,8,9]]
            Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
            The difference between any two elements in each array is less than or equal to 2.
            Note that the order of elements is not important.

        Example 2:
            Input: nums = [1,3,3,2,7,3], k = 3
            Output: []
            Explanation: It is not possible to divide the array satisfying all the conditions.
"""
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        nums = sorted(nums)
        rs = []
        for i in range(0, len(nums), 3):
            print(i)
            if nums[i + 1] - nums[i] <= k and nums[i + 2] - nums[i + 1] <= k and nums[i + 2] - nums[i] <= k:
                print('PASS')
                rs.append(nums[i: i + 3])
            else:
                print('FAILED')
                return []
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))
    # print(s.divideArray(nums = [1,3,3,2,7,3], k = 3))
    print(s.divideArray([15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2], k=2))