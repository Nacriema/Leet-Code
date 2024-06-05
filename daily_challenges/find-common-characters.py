""" 
Problem Statement:
    Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

        Example 1:
            Input: words = ["bella","label","roller"]
            Output: ["e","l","l"]

        Example 2:
            Input: words = ["cool","lock","cook"]
            Output: ["c","o"]
            
        Constraints:
            * 1 <= words.length <= 100
            * 1 <= words[i].length <= 100
            * words[i] consists of lowercase English letters.
"""
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Sort the words by the lenght of words
        if len(words) == 1:
            return list(words[0])
        word_counters = [Counter(word) for word in words]
        word_counters = sorted(word_counters, key=lambda x: len(x))
        
        first = word_counters[0]
        rs = []
        for letter, freq in first.items():
            flag = True
            min_so_far = freq
            for other in word_counters[1:]:
                if letter not in other.keys():
                    flag = False
                    break
                else:
                    min_so_far = min(min_so_far, other.get(letter))
            if flag:
                rs.extend([letter] * min_so_far)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(words = ["bella","label","roller"]))
    print(s.commonChars(words = ["cool","lock","cook"]))
    print(s.commonChars(words = ["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]))