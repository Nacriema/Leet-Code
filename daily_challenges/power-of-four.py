"""
    Problem statement:
        Given an integer n, return true if it is a power of four. Otherwise return false.
        
        An integer is a power of four, it there exist an integer x such that n == 4^x
        
        Example 1:
            Input: n = 16
            Output: true
            
        Example 2:
            Input: n = 5
            Output: false
            
        Example 3:
            Input: n = 1
            Output: true
            
        Constraints:
            * -2^31 <= n <= 2^31 - 1
            
        Follow up: Could you solve it wiout loops/recursion ? 
"""
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """ 
            Not use for loop
        """
        if n <= 0: return False
        return math.log(n, 4).is_integer()
    
    def isPowerOfFour_(self, n: int) -> bool:
        """ 
            Use for loop to check
        """
        if n <= 0: return False
        while float(n).is_integer() and n > 1:
            n /= 4
        print(n)
        return float(n).is_integer()
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.isPowerOfFour_(n=64))
    print(s.isPowerOfFour_(n=5))
    # print(s.isPowerOfFour(n=1))