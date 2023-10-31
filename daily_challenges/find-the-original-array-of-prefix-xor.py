""" 
    Problem statement:
        You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
            * pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
        Note that ^ denote the bitwise-zor operation.
        It can be proven that the answer is unique.
        
        Example 1:
            Input: pref = [5,2,0,3,1]
            Output: [5,7,2,3,2]
            Explanation: From the array [5,7,2,3,2] we have the following:
                - pref[0] = 5.
                - pref[1] = 5 ^ 7 = 2.
                - pref[2] = 5 ^ 7 ^ 2 = 0.
                - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
                - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
                
        Example 2:
            Input: pref = [13]
            Output: [13]
            Explanation: We have pref[0] = arr[0] = 13.
            
        Constraints:
            * 1 <= pref.length <= 10^5
            * 0 <= pref[i] <= 10^6
"""
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """ 
            NOTE: Invert of the xor is xor
            a ^ b = c <=> a = c ^ b; b = c ^ a
            
            XOR is associative and commutative
            
            Proof:
                a ^ b = c 
                c ^ a ^ b = c ^ c
                c ^ a ^ b ^ b = 0 ^ b
                c ^ a = b
        """
        rs = [pref[0]]
        for i in range(0, len(pref) - 1):
            rs.append(pref[i] ^ pref[i + 1])
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findArray(pref = [5, 2, 0, 3, 1]))
    print(s.findArray(pref = [13]))