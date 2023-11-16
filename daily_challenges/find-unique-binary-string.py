""" 
    Problem statement:
        Given an array of strings nums containing n unique binary strings each of length n, 
        return a binary string of length n that does not appear in nums. 
        If there are multiple answers, you may return any of them.

        Example 1:
            Input: nums = ["01","10"]
            Output: "11"
            Explanation: "11" does not appear in nums. "00" would also be correct.
            
        Example 2:
            Input: nums = ["00","01"]
            Output: "11"
            Explanation: "11" does not appear in nums. "10" would also be correct.
            
        Example 3:
            Input: nums = ["111","011","001"]
            Output: "101"
            Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

        Constraints:
            * n == nums.length
            * 1 <= n <= 16
            * nums[i].length == n
            * nums[i] is either '0' or '1'.
            * All the strings of nums are unique.
            
        Hints:
            * We can convert the given strings into base 10 integer
            * Can we use recursion to generate all possible strings
"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def get_binary_string(number, length):
            binary = bin(number)[2:]  # Convert number to binary string, remove '0b' prefix
            binary = binary.zfill(length)  # Pad the binary string with leading zeros if necessary
            return binary

        base_length = len(nums[0])
        base_10 = [int(num, 2) for num in nums]
        full_set = set(range(2**base_length))
        base_10_set = set(base_10)
        missing = full_set.difference(base_10_set)
        missing_list = list(missing)
        return get_binary_string(missing_list[0], base_length)

if __name__ == '__main__':
    s = Solution()
    print(s.findDifferentBinaryString(nums = ["01","10"]))
    print(s.findDifferentBinaryString(nums = ["00","01"]))
    print(s.findDifferentBinaryString(nums = ["111","011","001"]))