""" 
    Problem statement:
        Given an integer array nums, return the length of the longest strictly increasing subsequence.
        
        Example 1:
            Input: nums = [10,9,2,5,3,7,101,18]
            Output: 4
            Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

        Example 2:
            Input: nums = [0,1,0,3,2,3]
            Output: 4

        Example 3:
            Input: nums = [7,7,7,7,7,7,7]
            Output: 1

        Constraints:
            * 1 <= nums.length <= 2500
            * -10^4 <= nums[i] <= 10^4

        Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity ?
        
        Hints:
            * 
"""
from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        ans.append(nums[0])
        
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                # Find the right most value less than x
                index = bisect.bisect_left(ans, nums[i])
                ans[index] = nums[i]
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS(nums = [0,1,0,3,2,3]))
    print(s.lengthOfLIS(nums = [7,7,7,7,7,7,7]))