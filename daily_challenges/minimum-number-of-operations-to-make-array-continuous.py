"""
    Problem statement:
        You are given an integer array nums. In one operation, you can replace any element in nums with any
        integer.

        nums is considered continuous if both of the conditions are fulfilled:
            * All elements in nums are unique.
            * The difference between the maximum element and the minimum element in nums equals to
            nums.length - 1
        For example, nums = [4, 2, 5, 3] is continuous, but num = [1, 2, 3, 5, 6] is not continuous.

        Return the minimum number of operations to make nums continuous.

        Example 1:
            Input: nums = [4,2,5,3]
            Output: 0
            Explanation: nums is already continuous.

        Example 2:
            Input: nums = [1,2,3,5,6]
            Output: 1
            Explanation: One possible solution is to change the last element to 4.
            The resulting array is [1,2,3,5,4], which is continuous.

        Example 3:
            Input: nums = [1,10,100,1000]
            Output: 3
            Explanation: One possible solution is to:
            - Change the second element to 2.
            - Change the third element to 3.
            - Change the fourth element to 4.
            The resulting array is [1,2,3,4], which is continuous.4

        Constraints:
            1 <= nums.length <= 10^5
            1 <= nums[i] <= 10^9

        Hints:
            * Sort the array first
            * For every index do a binary search to get the possible right end of the window and calculate the possible answer.
"""
from typing import List
from bisect import bisect_right


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        For each item:
        Set it left bound -> right bound = left + len(nums) - 1
        Find the index of right bound in the sorted array, use binary search

        What happend if nums is duplicates
        """
        ans = len(nums)
        unique_nums = sorted(set(nums))
        print(f"Sorted nums: {nums}")
        
        for i in range(len(unique_nums)):
            left = unique_nums[i]
            right = left + len(nums) - 1
            j = bisect_right(unique_nums, right)
            print(f'Right: {right}, Insert index: {j}')
            ans = min(ans, len(nums) - (j - i))
        return ans

if __name__ == '__main__':
    s = Solution()

    # print(s.minOperations(nums=[4, 2, 5, 3]))
    # print(s.minOperations(nums=[1, 2, 3, 5, 6]))
    # print(s.minOperations(nums=[1, 10, 100, 1000]))
    # print(s.minOperations(nums=[8, 5, 9, 9, 8, 4]))
    print(s.minOperations(nums=[41, 33, 29, 33, 35, 26, 47, 24, 18, 28]))