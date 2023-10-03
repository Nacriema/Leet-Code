"""
    Problem Statement:
        You are given a large integer represent as an integer array digits, where each digits[i] is the ith
        digit of the integer. The digit are ordered from most significant to least significant in left-to-right
        order. The large integer does not contains any leading 0's
        
        Increment the large integer by one and return the resulting array of digits.

    Example 1:
        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4].

    Example 2:
        Input: digits = [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
        Incrementing by one gives 4321 + 1 = 4322.
        Thus, the result should be [4,3,2,2].

    Example 3:
        Input: digits = [9]
        Output: [1,0]
        Explanation: The array represents the integer 9.
        Incrementing by one gives 9 + 1 = 10.
        Thus, the result should be [1,0].
    
        Constraints:
            * 1 <= digits.length <= 100
            * 0 <= digits[i] <= 9
            * digits does not contains any leading 0's
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Edge case
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            # Do some math calculator
            rem = 0
            for i in range(len(digits) - 1, -1, -1):
                if i == len(digits) - 1:
                    total = digits[i] + rem + 1
                else:
                    total = digits[i] + rem
                if total >= 10:
                    rem = 1
                    digits[i] = total - 10
                    if i == 0:
                        digits = [1] + digits
                else:
                    rem = 0
                    digits[i] = total
                if rem == 0:
                    return digits
            return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne(digits=[1,2,3]))
    print(s.plusOne(digits=[4,3,2,1]))
    print(s.plusOne(digits=[9]))
    print(s.plusOne(digits=[9, 9, 9]))