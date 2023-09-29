"""
    Problem Statement:
        An array is monotonic if it is either monotone increasing or monotone decreasing.
        An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An 
        array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
        
        Given an integer array nums, return true if the given array is monotonic, or false otherwise.
        
        Example 1:
            Input: nums = [1,2,2,3]
            Output: true
            
        Example 2:
            Input: nums = [6,5,4,4]
            Output: true

        Example 3:
            Input: nums = [1,3,2]
            Output: false
            
    Constraints:
        * 1 <= nums.length <= 10^5
        * -10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        strict_increase = False
        strict_decrease = False
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                strict_decrease = True
            elif nums[i] < nums[i + 1]:
                strict_increase = True
            
            # Check the stop condition, when both of them are true
            if strict_increase and strict_decrease:
                return False
        
        # Pass all check
        return True
    
if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic(nums=[1,2,2,3]))
    print(s.isMonotonic(nums=[6,5,4,4]))
    print(s.isMonotonic(nums=[1,3,2]))