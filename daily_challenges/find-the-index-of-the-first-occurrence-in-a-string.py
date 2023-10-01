"""
    Problem Statement:
        Given two strings needle and haystack, return the index of the first occurence of needle in haystack
        or -1 if needle is not part of haystack.

    Example 1:
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: "sad" occurs at index 0 and 6.
        The first occurrence is at index 0, so we return 0.

    Example 2:
        Input: haystack = "leetcode", needle = "leeto"
        Output: -1
        Explanation: "leeto" did not occur in "leetcode", so we return -1.

    Constraints:
        * 1 <= haystack.length, needle.length <= 10^4
        * haystack and needle consist of only lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
            My implementation:
                - Reconstruct the array of LPS (The prefix, also the suffix)

            There are many solutions
                - Use built-in function (find, index)
                - Use naive method (took O(mn) in time complexity)
                - Use KMP algorithm (Took O(m+n) in time complexity)
        """
        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack="sadbutsad", needle="sad"))
    print(s.strStr(haystack="leetcode", needle="leeto"))