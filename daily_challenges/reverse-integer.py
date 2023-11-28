""" 
    Problem statement:
        Given a signed 32-bit integer x, return x with its digits reversed. 
        If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

        Example 1:
            Input: x = 123
            Output: 321

        Example 2:
            Input: x = -123
            Output: -321
        
        Example 3:
            Input: x = 120
            Output: 21

        Constraints:
            * -2^31 <= x <= 2^31 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = lambda a: (a > 0) - (a < 0)  # Return 1 or -1 or 0
        x_str = str(sign(x) * x)
        x_str_reversed = x_str[::-1]
        x_reversed = int(x_str_reversed)
        
        if -2**31 <= sign(x) * x_reversed <= 2**31 - 1:
            return sign(x) * x_reversed
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(x=123))
    print(s.reverse(x=-123))
    print(s.reverse(x=120))
    print(s.reverse(x=0))