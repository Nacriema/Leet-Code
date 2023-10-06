"""
    Problem statement:
        Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of thoese integers.
        Return the maximum product you can get.

    Example 1:
        Input: n = 2
        Output: 1
        Explanation: 2 = 1 + 1, 1 × 1 = 1.

    Example 2:
        Input: n = 10
        Output: 36
        Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

    Constraints:
        * 2 <= n <= 58

    Hints:
        * There is a simple O(n) solution to this problem
        * You may check the breaking results of n ranging from 7 to 10 to discover the regularities.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        count = 0
        while n >= 5:
            n -= 3
            count += 1
        print(f'Reduce: {n}, Number of 3: {count}')
        if count > 0:
            if n == 4: 
                return 3**count * 2 * 2
            elif n == 3:
                return 3**(count + 1)
            elif n == 2:
                return 3 ** count * 2
        else: 
            if n == 4:
                return 2 * 2
            elif n == 3:
                return 2
            else:
                return 1


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(n=2))
    print(s.integerBreak(n=10))
    print(s.integerBreak(n=20))
    print(s.integerBreak(n=4))
