""" 
    Problem statement: 
        Given a string s, return the number of homogeneous substrings of s. Since the answer may be too large, return it modulo 10^9+7
        A string is homogeneous if all the characters of the string are the same.
        A substring is a continuous sequence of character within a string.
        
        Example 1:
            Input: s = "abbcccaa"
            Output: 13
            Explanation: The homogenous substrings are listed as below:
                "a"   appears 3 times.
                "aa"  appears 1 time.
                "b"   appears 2 times.
                "bb"  appears 1 time.
                "c"   appears 3 times.
                "cc"  appears 2 times.
                "ccc" appears 1 time.
                3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
            
        Example 2:
            Input: s = "xy"
            Output: 2
            Explanation: The homogenous substrings are "x" and "y".

        Example 3:
            Input: s = "zzzzz"
            Output: 15
            
        Constraints:
            * 1 <= s.length <= 105
            * s consists of lowercase letters.
"""
class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1: return 1
        
        curr_continuous_cout = 1
        prev_char = s[0]
        rs = 0
        
        for i in range(1, len(s)):
            if s[i] == prev_char:
                curr_continuous_cout += 1
            else:
                print(f'Found {curr_continuous_cout} charracters {prev_char} !!')
                rs += (curr_continuous_cout * (curr_continuous_cout + 1) // 2)
                curr_continuous_cout = 1
                prev_char = s[i]
        
        print(f'Found {curr_continuous_cout} charracters {prev_char} !!')
        rs += (curr_continuous_cout * (curr_continuous_cout + 1) // 2)
        return rs
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.countHomogenous(s = "abbcccaa"))
    print(s.countHomogenous(s = "xy"))
    print(s.countHomogenous(s = "zzzzz"))
