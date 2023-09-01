"""
    Problem Statement:
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

        Example 1:
            Input: n = 2
            Output: [0,1,1]
            Explanation:
                0 --> b'0'  --> 0
                1 --> b'1'  --> 1
                2 --> b'10' --> 1
        
        Example 2:
            Input: n = 5
            Output: [0,1,1,2,1,2]
            Explanation:
                0 --> b'0'   --> 0
                1 --> b'1'   --> 1
                2 --> b'10'  --> 1
                3 --> b'11'  --> 2
                4 --> b'100' --> 1
                5 --> b'101' --> 2
    
    Constrains: 
        * 0 <= n <= 10^5

    Follow up:
        * It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
        * Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

        
    # FIND THE RULE
    0 -> 0
    1 -> 1
    2 -> 1
    3 -> 2
    4 -> 1
    5 -> 2     

    
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
            Use built-in function of Python and single lop -> like O(n)
        """
        return list(map(lambda x: bin(x).count('1'), range(0, n+1)))


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(n=5))