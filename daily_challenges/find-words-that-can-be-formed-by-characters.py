"""
    Problem statement:
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once).
        Return the sum of lengths of all good strings in words.

        Example 1:
            Input: words = ["cat","bt","hat","tree"], chars = "atach"
            Output: 6
            Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

        Example 2:
            Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
            Output: 10
            Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

        Constraints:
            * 1 <= words.length <= 1000
            * 1 <= words[i].length, chars.length <= 100
            * words[i] and chars consist of lowercase English letters.
"""
from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """ 
            This code is supported in Python 3.10
        """
        char_counter = Counter(chars)
        total = 0
        for word in words:
            word_counter = Counter(word)
            if word_counter <= char_counter:
                total += len(word)
        return total
    

if __name__ == '__main__':
    s = Solution()
    print(s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
    print(s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))