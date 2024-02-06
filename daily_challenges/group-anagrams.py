""" 
    Problem statement:  
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


        Example 1:
            Input: strs = ["eat","tea","tan","ate","nat","bat"]
            Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

        Example 2:
            Input: strs = [""]
            Output: [[""]]

        Example 3:
            Input: strs = ["a"]
            Output: [["a"]]

        Constraints:
            * 1 <= strs.length <= 10^4
            * 0 <= strs[i].length <= 100
            * strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import Counter

class Solution:
    def groupAnagrams_NOTOPTIMIZED(self, strs: List[str]) -> List[List[str]]:
        table = dict()   # type: dict
        for s in strs:
            tmp = table.get(frozenset(Counter(s).items()), [])
            tmp.append(s)
            table[frozenset(Counter(s).items())] = tmp
        print(table)
        return list(table.values())
    
    # TODO: Find another method !!!

if __name__ == '__main__':
    s = Solution()
    # print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    # print(s.groupAnagrams(strs = [""]))
    # print(s.groupAnagrams(strs = ["a"]))
    print(s.groupAnagrams_NOTOPTIMIZED(strs=["ddddddddddg","dgggggggggg"]))
