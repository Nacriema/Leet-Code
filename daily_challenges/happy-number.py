"""
    Problem statement:
        Write an algorithm to determine if a number n is happy.
        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.

        Example 1:
            Input: n = 19
            Output: true
            Explanation:
                1^2 + 9^2 = 82
                8^2 + 2^2 = 68
                6^2 + 8^2 = 100
                1^2 + 0^2 + 0^2 = 1

        Example 2:
            Input: n = 2
            Output: false

        Constraints:
            * 1 <= n <= 2^31 - 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def check(n: int):
            digits = [1] * len(str(n))
            count = len(str(n)) - 1
            while n != 0:
                digits[count] = n % 10
                n //= 10
                count -= 1
            tmp = 0
            for digit in digits:
                tmp += digit ** 2
            return tmp

        while n not in (4, 16, 37, 58, 89, 145, 42, 20):
            val = check(n)
            if n == 1:
                return True
            n = val
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(n=19))