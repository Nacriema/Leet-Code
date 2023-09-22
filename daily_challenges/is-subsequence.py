"""
    Problem Statement:
        Given two strings s and t, return True if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some
        (can be more) of the characters without disturbing the relative positions of the remaining characters.
        (i.e. "ace" is a subsequence of "abcde" while "aec" is not)

    Example 1: 
        Input: s = "abc", t = "ahbgdc"
        Output: true

    Example 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false

    Constraints:
        * 0 <= s.length <= 100
        * 0 <= t.length <= 10^4
        * s and t consist only of lowercase English letters.

    Follow up: Suppose there are lots of incoming s, say s_1, s_2, ... s_k where k > 10^9 and you want to check 
    one by one to see if t has its subsequence. In this scenario, how would you change your code ?
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        """
        for char in t:
            if len(s) == 0:
                return True
            else:
                if s[0] == char:
                    s = s[1:]
        return len(s) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence(s="abc", t="ahbgdc"))
    print(s.isSubsequence(s="axc", t="ahbgdc"))
