""" 
    Problem Statement:
        URL: https://leetcode.com/problems/word-pattern/description/
        290. Word Pattern
        Given a pattern and a string s, find if s follows the same pattern.
        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

        Example 1:
            Input: pattern = "abba", s = "dog cat cat dog"
            Output: true

        Example 2:
            Input: pattern = "abba", s = "dog cat cat fish"
            Output: false

        Example 3:
            Input: pattern = "aaaa", s = "dog cat cat dog"
            Output: false

        Constraints:
            * 1 <= pattern.length <= 300
            * pattern contains only lower-case English letters.
            * 1 <= s.length <= 3000
            * s contains only lowercase English letters and spaces ' '.
            * s does not contain any leading or trailing spaces.
            * All the words in s are separated by a single space.
"""
from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = defaultdict(str)
        table2 = defaultdict(str)
        s_p = s.split(' ')
        if len(pattern) != len(s_p): return False
        for c, w in zip(pattern, s.split(' ')):
            if len(table[c]) and table[c] != w:
                return False
            else: 
                table[c] = w
            if len(table2[w]) and table2[w] != c:
                return False
            else: 
                table2[w] = c
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))
    print(s.wordPattern(pattern = "abba", s = "dog cat cat fish"))
    print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))