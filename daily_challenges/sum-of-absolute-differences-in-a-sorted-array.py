""" 
    Problem statement:
        You are given an integer array nums sorted in non-decreasing order.

        Build and return an integer array result in the same length as nums such that result[i] is equal to
        the summarization of absolute differences between nums[i] and all the otehr elements in the array.

        In other words, result[i] is equal to sum(|nums[i] - nums[j]|) where 0 <= j < nums.length and j != i 
        (0-indexed)

        Example 1:
            Input: nums = [2,3,5]
            Output: [4,3,5]
            Explanation: Assuming the arrays are 0-indexed, then
                result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
                result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
                result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

                
        Example 2:
            Input: nums = [1,4,6,8,10]
            Output: [24,15,13,15,21]

        Constraints:
            * 2 <= nums.length <= 10^5
            * 1 <= nums[i] <= nums[i + 1] <= 10^4

        Hint:
            * Absolute difference is the same as max(a, b) - min(a, b). How can you use this fact with the fact 
            that the array is sorted            
"""
from typing import List

class Solution:
    def getSumAbsoluteDifferences_SLOW(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        first_sum = 0
        rs = []
        for i in range(len(nums)):
            # print(f'Index: {i}')
            # print(f'Sum of number smaller: {first_sum}, total number: {i}')
            # print(f'Sum of number greater: {total - first_sum - nums[i]}, total number: {len(nums) - i - 1}')
            tmp = nums[i] * i - first_sum + (total - first_sum - nums[i]) - nums[i] * (len(nums) - i - 1)
            rs.append(tmp)
            first_sum += nums[i]
        return rs
    
    
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        # Prefix sum
        n = len(nums)
        ans = [0] * n
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i, num in enumerate(nums):
            ans[i] = ((2 * i - n) * num - 2 * prefix_sum[i] + prefix_sum[n])

        return ans
        """

        n = len(nums)
        diff = sum(nums)
        ans = [0] * n

        for i, num in enumerate(nums):
            ans[i] = (2 * i - n) * num + diff
            diff -= 2 * num

        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.getSumAbsoluteDifferences(nums = [2,3,5]))
    print(s.getSumAbsoluteDifferences(nums = [1,4,6,8,10]))