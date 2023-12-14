"""
    Problem statement:
        Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

        Example 1:
            Input: nums = [1,2,3,1], k = 3
            Output: true

        Example 2:
            Input: nums = [1,0,1,1], k = 1
            Output: true

        Example 3:
            Input: nums = [1,2,3,1,2,3], k = 2
            Output: false

        Constraints:
            * 1 <= nums.length <= 10^5
            * -10^9 <= nums[i] <= 10^9
            * 0 <= k <= 10^5
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()  # Table will store index of the last time the number it seen so far
        for id, num in enumerate(nums):
            if num not in table.keys():
                table.update({num: id})
            else:
                if abs(id - table.get(num)) <= k:
                    return True
                else:
                    table[num] = id
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
    print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))

