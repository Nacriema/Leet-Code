""" 
    Problem statement:
        Given an array nums of size n, return the majority element.
        The majority element is the elememt that appear more than [n / 2] times. You may assume that the majority element always exits 
        in the array.
        
        Example 1:
            Input: nums = [3,2,3]
            Output: 3
            
        Example 2:
            Input: nums = [2,2,1,1,1,2,2]
            Output: 2

        Constraints:
            * n == nums.length
            * 1 <= n <= 5 * 10^4
            * -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ 
            For O(n) time complexity, we can use Booyer-Moore Algorithm
        """
        candidate = -1
        vote = 0
        
        for num in nums:
            if vote == 0:
                candidate = num
                vote = 1
            else:
                if num == candidate:
                    vote += 1
                else: 
                    vote -= 1
                    
        # Because the assumption that the majority element always exits in the array. 
        return candidate
    

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums = [3,2,3]))
    print(s.majorityElement(nums = [2,2,1,1,1,2,2]))
    print(s.majorityElement(nums = [3,3,4]))