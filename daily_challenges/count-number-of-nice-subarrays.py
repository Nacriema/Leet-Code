"""
    Problem statement:
        Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
        Return the number of nice sub-arrays.


        Example 1:
            Input: nums = [1,1,2,1,1], k = 3
            Output: 2
            Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

        Example 2:
            Input: nums = [2,4,6], k = 1
            Output: 0
            Explanation: There are no odd numbers in the array.

        Example 3:
            Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
            Output: 16

        Constraints:
            * 1 <= nums.length <= 50000
            * 1 <= nums[i] <= 10^5
            * 1 <= k <= nums.length

        Hint: 
            * After replacing each even by zero and every odd by one can we use PREFIX SUM to find answer ?
            * Can we use two pointers to count number of sub-arrays ?
            * Can we store indices of odd numbers and for each k indices count number of sub-arrays contains them ?
"""
from typing import List
from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_ids = deque([]) # creating a deque
        # O(n)
        for i, num in enumerate(nums):
            if num % 2 != 0:
                odd_ids.append(i)
        # Window sliding O(n)
        rs = 0
        for i in range(len(odd_ids)-k+1):
            # Calculate the combination
            num_even_left = odd_ids[i] if (i - 1 < 0) else odd_ids[i] - odd_ids[i - 1]  - 1
            num_even_right = len(nums) - 1 - odd_ids[-1] if (i + k >= len(odd_ids)) else odd_ids[i + k] - odd_ids[i + k - 1] - 1
            rs += (num_even_left + 1) * (num_even_right + 1)        
        return rs

if __name__ == '__main__':
    s = Solution()
    # print(s.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
    # print(s.numberOfSubarrays(nums = [2,4,6], k = 1))
    # print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
    print(s.numberOfSubarrays(nums=[2,2,2,1,2,2,1,2,2,1,2,2,2], k=2))