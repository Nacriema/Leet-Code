""" 
    Problem statement:
        Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
        A subarray is a contiguous part of an array.

        Example 1:
            Input: nums = [4,5,0,-2,-3,1], k = 5
            Output: 7
            Explanation: There are 7 subarrays with a sum divisible by k = 5:
            [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

        Example 2:
            Input: nums = [5], k = 9
            Output: 0

        Constraints:
            * 1 <= nums.length <= 3 * 10^4
            * -10^4 <= nums[i] <= 10^4
            * 2 <= k <= 10^4
"""
from typing import List
from math import comb


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """ 
            Calculate the cumulative sum % k
            If 0: number of 0s + comb(nb_0s , 2)
            else: comb(nb, 2)

            Since: 2 number in cumsum same remainder => their substraction also divided by k
        """
        table = dict()
        # Cumulative sum 
        tmp = nums[0] = nums[0] % k
        table.update({tmp: 1})
        for i in range(1, len(nums)):
            tmp += nums[i]
            nums[i] = tmp % k
            check_idx = table.get(nums[i], -1)
            if check_idx == -1:
                table.update({nums[i]: 1})
            else:
                table.update({nums[i]: check_idx + 1})
        cnt = 0
        for k, v in table.items():
            cnt += comb(v, 2)
            if k == 0:
                cnt += v
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
    print(s.subarraysDivByK(nums = [5], k = 9))