"""
    Problem Statement:
        There is a robot on an m x n grid. The robot is initially located at the TOP-LEFT CORNER. The robot
        tries to move to the BOTTOM-RIGHT-CORNER. The robot can only move either down or right at any point in time.
        Given the two integer m and n, return the number of possible unique paths that the robot can take to reach the 
        botton-right corner.

        Test case are generated so that the answer will be less than or equal to 2 * 10^9

        Example 1:
            Input : m = 3, n = 7
            Output: 28

        Example 2:
            Input : m = 3, n = 2
            Output: 3
            Explanation: From the top-left corner, there are total of 3 ways to reach the bottom-right corner:
                1. Right -> Down -> Down
                2. Down -> Down -> Right
                3. Down -> Right -> Down

        There are rule in this problem: May be we can solved this in O(1) ?

        To reach from top-left to right-bottom then:
            Number of Down = m - 1
            Number of Right = n - 1
            And the number of solutions be the number of permutation that we can have

        We have in total (m + n - 2) slots, we want to pick m - 1 random slot from them to fill the Down
        So we have:  (m + n - 2)C(m - 1)

        NOTE: nCr = n! / (r!(n-r)!), in python we can use math.factorial(n) to compute n!
"""
import operator as op
from functools import reduce


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            Implementation here
        """
        def ncr(n, r):
            r = min(r, n - r)
            numerator = reduce(op.mul, range(n, n - r, -1), 1)
            denominator = reduce(op.mul, range(1, r + 1), 1)
            return numerator // denominator

        return ncr(n=m+n-2, r=m-1)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(m=3, n=2))
    print(s.uniquePaths(m=3, n=7))

