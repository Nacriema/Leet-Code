"""
    Problem Statement:
        Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j]
        and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j]

        Return true if there is a 132 pattern in nums, otherwise return fasles

    Example 1:
        Input: nums = [1,2,3,4]
        Output: false
        Explanation: There is no 132 pattern in the sequence. 

    Example 2:
        Input: nums = [3,1,4,2]
        Output: true
        Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

    Example 3:
        Input: nums = [-1,3,2,0]
        Output: true
        Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

    Constraints:
        * n == nums.length 
        * 1 <= n <= 2 * 10^5
        * -10^9 <= nums[i] <= 10^9

    Hint: Use Stack !!
"""
from typing import List


class Solution:
    def find132pattern_NotPassed(self, nums: List[int]) -> bool:
        """
            92 / 103 cases
            Failed with case [3, 5, 0, 3, 4]
        """
        my_stack = []
        for i in range (len(nums)):
            largest_pop_value = None
            while(len(my_stack) and my_stack[-1] > nums[i]):
                val = my_stack.pop()  # First pop is the largest
                if largest_pop_value is None:
                    largest_pop_value = val
            my_stack.append(nums[i])
            print(f'Current num: {nums[i]}')
            print(f"My stack: {my_stack}")
            print(f'Largest pop value: {largest_pop_value}')
            print('==============')

            if len(my_stack) > 1 and largest_pop_value is not None and my_stack[0] < my_stack[-1] < largest_pop_value:
                return True
        return False
    



if __name__ == '__main__':
    s = Solution()
    # print(s.find132pattern(nums=[1, 2, 3, 4]))
    # print(s.find132pattern(nums=[3, 1, 4, 2]))
    # print(s.find132pattern(nums=[-1, 3, 2, 0]))
    # print(s.find132pattern(nums=[3, 5, 4]))
    print(s.find132pattern(nums=[3, 5, 0, 3, 4]))  # True because of 3, 5, 4 
    
