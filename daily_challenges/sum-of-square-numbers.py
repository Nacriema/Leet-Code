""" 
    Problem statement:
        Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

        Example 1:
            Input: c = 5
            Output: true
            Explanation: 1 * 1 + 2 * 2 = 5

        Example 2:
            Input: c = 3
            Output: false

        Constraints:
            * 0 <= c <= 2^31 - 1
"""
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True
        for i in range(math.ceil(math.sqrt(c))):
            print(i)
            remain = c - (i ** 2)
            tmp = int(math.sqrt(remain))
            if tmp ** 2 == remain:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.judgeSquareSum(c = 5))
    # print(s.judgeSquareSum(c = 3))
    # print(s.judgeSquareSum(c = 2))
    print(s.judgeSquareSum(c = 0))