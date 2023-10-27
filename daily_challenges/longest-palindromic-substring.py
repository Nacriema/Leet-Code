""" 
    Problem statement:
        Given a string s, return the longest palindromic substring in s.
        
    Example 1:
        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.

    Example 2:
        Input: s = "cbbd"
        Output: "bb"
    
    Constraints:
        * 1 <= s.length <= 1000
        * s consist of only digits and English letters.
        
    Hints:
        * How can we reuse a previously computed palindrome to compute a larger palindrome ?
        * If "aba" is a palindrome, is "xabax" a palindrome ? Similarity is "xabay" a palindrome ?
        * Complexity based hint:
            If we use brute-force and check whether for every start and end position a substring is a palindrome
            we have O(n^2) start-end pairs and O(n) palindromic checks.
            Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.
"""
class Solution:
    def longestPalindrome_BF(self, s: str) -> str:
        def isPalindrome(st: str):
            return st == st[::-1]
        
        rs = s[0]
        
        # Attempt 1: Use brute-force
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                tmp = s[i: j]
                if isPalindrome(tmp) and len(rs) < len(tmp):
                    rs = tmp
        return rs
    
    def longestPalindrome(self, s: str) -> str:
        """ 
            Use DP ?
        """
        def isPalindrome(st: str):
            return st == st[::-1]
        rs = s[0]
        
        
        pass
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome(s="babad"))
    # print(s.longestPalindrome(s="cbbd"))
    # print(s.longestPalindrome(s="a"))
    print(s.longestPalindrome(s="bb"))
    