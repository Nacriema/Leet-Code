"""
    Problem Statement:
        You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and substract its value from x. Note that this 
        modifies the array for future operations.
        
        Return the minimum number of operations to reduce x to exactly 0 if possible, otherwise return -1.
        
    Example 1: 
        Input: nums = [1,1,4,2,3], x = 5
        Output: 2
        Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
        
    Example 2:
        Input: nums = [5,6,7,8,9], x = 4
        Output: -1
        
    Example 3:
        Input: nums = [3,2,20,1,1,3], x = 10
        Output: 5
        Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
        
    Constraints: 
        * 1 <= nums.length <= 10^5
        * 1 <= nums[i] <= 10^4
        * 1 <= x <= 10^9
        
    Hint:
        * Think in reverse: instead of finding the minimum prefix + suffix -> finding the maximum subarray
        * Finding the maximum subarray such that the sum of this subarray = sum(nums) - x
        * Finding the maximum subarray is standard and can be done greedily
"""
from typing import List


class Solution:
    def TLE_minOperations(self, nums: List[int], x: int) -> int:
        
        # Finding the maximum subarray that have the specific sum 
        target = sum(nums) - x
        
        if target == 0:
            return len(nums)
        
        print(f"Target: {target}")
        rs = 0
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp == target:
                    print(f"Start: {i}, End: {j}")
                    rs = max(rs, (j - i + 1))
                    break
                elif tmp > target:
                    break
        
        print(f"Rs: {rs}")
        
        if rs == 0:
            return -1
        
        return len(nums) - rs
    
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        max_length = -1
        memo = {}
        memo[0] = -1  # Memo is dict that contains (sum(0 - index), index)
        
        tmp = 0
        
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp not in memo:
                memo[tmp] = i
            
            if tmp - target in memo and max_length  < i - memo[tmp - target]:
                print(f'Hit at index: {i}')
                max_length = i - memo[tmp - target]
        
        if max_length == -1:
            return max_length
        
        return len(nums) - max_length

if __name__ == '__main__':
    s = Solution()
    # print(s.minOperations(nums = [1,1,4,2,3], x = 5))
    # print(s.minOperations(nums = [5,6,7,8,9], x = 4))
    # print(s.minOperations(nums = [3,2,20,1,1,3], x = 10))
    print(s.minOperations(nums=[8828, 9581, 49, 9818, 9974, 9869, 9991,10000,10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], x=134365))  # Expected: 16