"""
    Problem statement:  
        Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character while preserving the order of characters.
        No two characters may map to the same character, but a character may map to itself.

        Example 1:
            Input: s = "egg", t = "add"
            Output: true

        Example 2:
            Input: s = "foo", t = "bar"
            Output: false

        Example 3:
            Input: s = "paper", t = "title"
            Output: true

        Constraints:
            * 1 <= s.length <= 5 * 10^4
            * t.length == s.length
            * s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic_(self, s: str, t: str) -> bool:
        # 1. Find the relation ship between 2 character
        table = dict()  # Lookup table (key: character in s, value: character in t that mapped)
        for a, b in zip(s, t):
            if b in table.values() and list(table.keys())[list(table.values()).index(b)] != a:
                return False
            if a not in table.keys():
                table.update({a: b})
            else:
                if table[a] != b:
                    return False
        return True
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped = set(zip(s, t))
        if len(zipped) == len(set(s)) == len(set(t)):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic(s="egg", t="add"))
    print(s.isIsomorphic(s="foo", t="bar"))
    print(s.isIsomorphic(s="paper", t="title"))
    print(s.isIsomorphic(s="badc", t="baba"))