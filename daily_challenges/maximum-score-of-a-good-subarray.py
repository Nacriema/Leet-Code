"""
    Problem statement:
        You are given an array of integers nums (0-indexed) and an integer k. The score of a subarray (i, j)
        is defined as min(nums[i], nums[i + 1], ..., nums[j]) * (j - i + 1). A good subarray where i <= k <= j
        
        Return the maximum possible score of a good subarray.

        Example 1: 
            Input: nums = [1,4,3,7,4,5], k = 3
            Output: 15
            Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

        Example 2:
            Input: nums = [5,5,4,5,4,1,1,1], k = 0
            Output: 20
            Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

        Constraints:
            * 1 <= nums.length <= 10^5
            * 1 <= nums[i] <= 2 * 10^4
            * 0 <= k < nums.length

        Brain Storming:
            * This problem is like the Greedy Algorithm.
"""
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # 1. Start with i == j == k
        i = j = k
        min_left = min_right = nums[k]
        max_so_far = nums[k]

        # 2. 
        while not(i == 0 and j == len(nums) -1):
            if i == 0:
                j += 1
                min_right = min(min_right, nums[j])
                max_so_far = max(max_so_far, min_right * (j - i + 1))
            elif j == len(nums) - 1:
                i -= 1
                min_left = min(min_left, nums[i])
                max_so_far = max(max_so_far, min_left * (j - i + 1))
            else:
                if nums[i - 1] >= nums[j + 1]:
                    i -= 1
                    min_left = min(min_left, nums[i])
                    max_so_far = max(max_so_far,  min_left * (j - i + 1))
                else:
                    j += 1
                    min_right = min(min_right, nums[j])
                    max_so_far = max(max_so_far, min_right * (j - i + 1))
        
        return max_so_far


if __name__ == '__main__':
    s = Solution()
    print(s.maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))
    print(s.maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))
    print(s.maximumScore(nums=[5], k=0))
