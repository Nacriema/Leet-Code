"""
    Problem statement:
        Given an array of integers nums sorted in non-decreasing order, find the start and ending position of a given target value.
        If target is not found in the array, return [-1, -1]
        You must write an algorithm with O(log n) runtime compexity.

        Example 1:
            Input: nums = [5,7,7,8,8,10], target = 8
            Output: [3,4]

        Example 2:
            Input: nums = [5,7,7,8,8,10], target = 6
            Output: [-1,-1]

        Example 3:
            Input: nums = [], target = 0
            Output: [-1,-1]

        Constraints:
            * 0 <= nums.length <= 105
            * -10^9 <= nums[i] <= 10^9
            * nums is a non-decreasing array.
            * -10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        def left_bound(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                if nums[mid] > target:
                    end = mid - 1
                if nums[mid] == target:
                    end = mid - 1
            if start > len(nums) - 1 or nums[start] != target:
                return -1
            return start

        def right_bound(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                if nums[mid] > target:
                    end = mid - 1
                if nums[mid] == target:
                    start = mid + 1
            if end < 0 or nums[end] != target:
                return -1
            return end

        l = left_bound(low, high)
        r = right_bound(low, high)

        return [l, r]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums=[5,7,7,8,8,10], target=8))
    print(s.searchRange(nums=[5,7,7,8,8,10], target=6))
    print(nums=[], target=0)