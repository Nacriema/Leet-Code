"""
    Problem Statement:
        Given an integer array nums, move all even integers at the begining of the array followed by all the odd integers.
        
        Return any array that satisfies this condition.
        
    Example 1:
        Input: nums = [3,1,2,4]
        Output: [2,4,3,1]
        Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
        
    Example 2:
        Input: nums = [0]
        Output: [0]
        
    Constraints:
        * 1 <= nums.length <= 5000
        * 0 <= nums[i] <= 5000
"""
from typing import List


class Solution:
    def sortArrayByParity_SLOW(self, nums: List[int]) -> List[int]:
        odds = []
        curr_idx = 0
        while curr_idx < len(nums) - 1 and curr_idx >= 0:
            if nums[curr_idx] % 2 == 1:
                odds.append(nums.pop(curr_idx))
                curr_idx -= 1
            else:
                curr_idx += 1
        return nums + odds
    

if __name__ == '__main__':
    s = Solution()
    # print(s.sortArrayByParity(nums=[3,1,2,4]))  # Return [2, 4, 3, 1]
    # print(s.sortArrayByParity(nums=[0]))
    print(s.sortArrayByParity(nums=[1,3]))