""" 
    Problem statement:
        You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. 
        
        For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
            * 0 <= i < j < nums.length
            * nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        
        Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10^9 + 7.

        Example 1:
            Input: nums = [42,11,1,97]
            Output: 2
            Explanation: The two pairs are:
            - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
            - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
            
        Example 2:
            Input: nums = [13,10,35,24,76]
            Output: 4
        

        Constraints:
            * 1 <= nums.length <= 10^5
            * 0 <= nums[i] <= 10^9
"""
from typing import List
from collections import defaultdict, Counter
import math

class Solution:
    def countNicePairs_SLOW(self, nums: List[int]) -> int:
        def revert(num):
            # converting number to string 
            string = str(num) 
            # reversing the string 
            string = list(string) 
            string.reverse() 
            string = ''.join(string) 
            # converting string to integer 
            num = int(string) 
            # returning integer 
            return num
        
        table = defaultdict(lambda : 0)  # type: dict
        for num in nums:
            tmp = num - revert(num)
            table[tmp] += 1
        rs = 0
        for v in table.values():
            if v >= 2:
                rs += math.comb(v, 2)
                rs %= 10 ** 9 + 7
        return rs
    
    def countNicePairs(self, nums: List[int]) -> int:
        modified = [i - int(str(i)[::-1]) for i in nums]

        count = 0
        for i in Counter(modified).values():
            count += i*(i -1)//2 
        return count%(1000000000 + 7)
    

if __name__ == '__main__':
    s = Solution()
    print(s.countNicePairs(nums=[42, 11, 1, 97]))
    print(s.countNicePairs(nums=[13, 10, 35, 24, 76]))
    