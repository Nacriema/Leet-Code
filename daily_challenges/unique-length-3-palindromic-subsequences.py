""" 
    Problem statement:
        Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
        
        Note that even if there are many multiple ways to obtain the same subsequence, it is still only counted once.
        
        A palindrome is a string that reads the same forwards and backwards.
        
        A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
        
        For example, "ace" is a subsequence of "abcde".
        
        Example 1:
            Input: s = "aabca"
            Output: 3
            Explanation: The 3 palindromic subsequences of length 3 are:
                - "aba" (subsequence of "aabca")
                - "aaa" (subsequence of "aabca")
                - "aca" (subsequence of "aabca")
                
        Example 2:
            Input: s = "adc"
            Output: 0
            Explanation: There are no palindromic subsequences of length 3 in "adc".
            
        
        Example 3:
            Input: s = "bbcbaba"
            Output: 4
            Explanation: The 4 palindromic subsequences of length 3 are:
                - "bbb" (subsequence of "bbcbaba")
                - "bcb" (subsequence of "bbcbaba")
                - "bab" (subsequence of "bbcbaba")
                - "aba" (subsequence of "bbcbaba")
        
        Constraints:
            * 3 <= s.length <= 10^5
            * s consists of only lowercase English letters.
"""
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def countPalindromicSubsequence_SLOW(self, s: str) -> int:
        table = dict()  # type:dict
        for i in range(len(s)):
            char = s[i]
            tmp = table.get(char, [])
            tmp.append(i)
            table[char] = tmp
        print(f'Table: {table}')
        rs = []
        for k, v in table.items():
            if len(v) == 1:
                continue
            elif len(v) == 2 and v[0] == v[1]:
                continue
            else:
                if len(v) >= 3:
                    rs.append(f"{k}"*3)
                for j in range(v[0], v[-1]):
                    if s[j] != k:
                        rs.append(f"{k}{s[j]}{k}")
        rs = set(rs)
        return len(rs)
    
    def countPalindromicSubsequence(self, s: str) -> int:
        idx = defaultdict(list)
        for i,c in enumerate(s):
            idx[c].append(i)
        ans = 0
        
        print(f'Table idx: {idx}')
        
        for c, i in idx.items():
            if len(i) < 2:
                continue
            if len(i) > 2:
                ans += 1
            for k, j in idx.items():
                if c == k:
                    continue
                if bisect_left(j, i[0]) < bisect_left(j, i[-1]):
                    ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.countPalindromicSubsequence(s = "aabca"))
    # print(s.countPalindromicSubsequence(s = "adc"))
    # print(s.countPalindromicSubsequence(s = "bbcbaba"))
    print(s.countPalindromicSubsequence(s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"))
