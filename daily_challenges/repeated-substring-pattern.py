""" 
    Problem statement:
        Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

        Example 1:
            Input: s = "abab"
            Output: true
            Explanation: It is the substring "ab" twice.

        Example 2:
            Input: s = "aba"
            Output: false

        Example 3:
            Input: s = "abcabcabcabc"
            Output: true
            Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

        Constraints:
            * 1 <= s.length <= 10^4
            * s consists of lowercase English letters.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # String concatenation 
        check_string = s[1: len(s)] + s[:len(s) - 1]
        for i in range(0, len(check_string) - len(s) + 1):
            if check_string[i: i + len(s)] == s:
                return True
        return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        if s in t [1:-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.repeatedSubstringPattern(s = "abab"))
    # print(s.repeatedSubstringPattern(s = "aba"))
    # print(s.repeatedSubstringPattern(s = "abcabcabcabc"))
    print(s.repeatedSubstringPattern(s="abaababaab"))
