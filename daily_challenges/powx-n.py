""" 
    Problem Statement:
        URL: https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150
        50. Pow(x, n)
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

        Example 1:
            Input: x = 2.00000, n = 10
            Output: 1024.00000

        Example 2:
            Input: x = 2.10000, n = 3
            Output: 9.26100

        Example 3:
            Input: x = 2.00000, n = -2
            Output: 0.25000
            Explanation: 2-2 = 1/22 = 1/4 = 0.25

        Constraints:
            * -100.0 < x < 100.0
            * -2^31 <= n <= 2^31-1
            * n is an integer.
            * Either x is not zero or n > 0.
            * -10^4 <= xn <= 10^4
"""
import time

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exponent):
            print(f'Exponent: {exponent}')
            time.sleep(2)
            if exponent == 0:
                return 1
            elif exponent < 0:
                return 1 / power(base, -exponent)
            elif exponent % 2 == 0:
                half_power = power(base, exponent // 2)
                return half_power * half_power
            else:
                return base * power(base, exponent - 1)
        return power(base=x, exponent=n)


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(x = 2.00000, n = 10))
    print(s.myPow(x = 2.10000, n = 3))
    print(s.myPow(x = 2.00000, n = -2))