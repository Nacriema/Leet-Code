""" 
    Problem statement:
        Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

        Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. 
        If there are multiple elements with the largest value, pick the smallest i.
        
        Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
        Reduce nums[i] to nextLargest.
        
        Return the number of operations to make all elements in nums equal.


        Example 1:
            Input: nums = [5,1,3]
            Output: 3
            Explanation: 
                It takes 3 operations to make all elements in nums equal:
                1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
                2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
                3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].
        
        Example 2:
            Input: nums = [1,1,1]
            Output: 0
            Explanation: All elements in nums are already equal.
        
        Example 3:
            Input: nums = [1,1,2,2,3]
            Output: 4
            Explanation: 
                It takes 4 operations to make all elements in nums equal:
                1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,2].
                2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1,2,2].
                3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,1,2].
                4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,1].

        Constraints:
            * 1 <= nums.length <= 5 * 10^4
            * 1 <= nums[i] <= 5 * 10^4
            
        Hints:
            * Sort the array
            * Try to reduce all elements with maximum value to the next maximum value in one operation.
"""
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        print(f'Sorted nums: {nums}')
        largest = nums[-1]
        idx = len(nums) - 1
        ans = 1
        rs = 0
        
        while largest != nums[0] and idx > 0:
            if nums[idx] == nums[idx - 1]:
                ans += 1
            else:
                print(f'Find boundary: {nums[idx]} and {nums[idx - 1]}')
                print(f'Current consecutive max val: {ans}')
                print(f'Will took: {len(nums) - idx} action to finish ...')
                rs += len(nums) - idx
                print(f'Total so far: {rs}')
                ans = 1
            idx -= 1
            
        return rs
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.reductionOperations(nums = [5,1,3]))
    # print(s.reductionOperations(nums = [1,1,1]))
    # print(s.reductionOperations(nums = [1,1,2,2,3]))
    # print(s.reductionOperations(nums = [7,9,10,8,6,4,1,5,2,3]))  # Expected 45