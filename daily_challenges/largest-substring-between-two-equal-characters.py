"""
    Problem statement:
        Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. 
        If there is no such substring return -1.
        A substring is a contiguous sequence of characters within a string.

        Example 1:
            Input: s = "aa"
            Output: 0
            Explanation: The optimal substring here is an empty substring between the two 'a's.

        Example 2:
            Input: s = "abca"
            Output: 2
            Explanation: The optimal substring here is "bc".

        Example 3:
            Input: s = "cbzxy"
            Output: -1
            Explanation: There are no characters that appear twice in s.

        Constraints:
            * 1 <= s.length <= 300
            * s contains only lowercase English letters.
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        table = {}
        rs = -1
        for i, char in enumerate(s):
            tmp = table.get(char, [])
            tmp.append(i)
            if len(tmp) >=2:
                if tmp[-1] - tmp[0] - 1 >= 0:
                    rs = max(rs, tmp[-1] - tmp[0] - 1)
            table[char] = tmp
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthBetweenEqualCharacters(s="aa"))
    print(s.maxLengthBetweenEqualCharacters(s="abca"))
    print(s.maxLengthBetweenEqualCharacters(s="cbzxy"))
