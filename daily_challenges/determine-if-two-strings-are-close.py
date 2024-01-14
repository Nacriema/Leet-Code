"""
    Two strings are considered close if you can attain one from the other using the following operations:
    
    * Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    * Operation 2: Transform every occurrence of one existing character into another existing character, 
    and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

    You can use the operations on either string as many times as necessary.
    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    Example 1:
        Input: word1 = "abc", word2 = "bca"
        Output: true
        Explanation: You can attain word2 from word1 in 2 operations.
        Apply Operation 1: "abc" -> "acb"
        Apply Operation 1: "acb" -> "bca"

    Example 2:
        Input: word1 = "a", word2 = "aa"
        Output: false
        Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

    Example 3:
        Input: word1 = "cabbba", word2 = "abbccc"
        Output: true
        Explanation: You can attain word2 from word1 in 3 operations.
        Apply Operation 1: "cabbba" -> "caabbb"
        Apply Operation 2: "caabbb" -> "baaccc"
        Apply Operation 2: "baaccc" -> "abbccc"

    Constraints:
        * 1 <= word1.length, word2.length <= 10^5
        * word1 and word2 contain only lowercase English letters.
"""
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Not only the cardinality, but also the cardinal of characters must be the same
        word1_c = Counter(word1)
        word2_c = Counter(word2)        
        word1_val_sorted = sorted(word1_c.values())
        word2_val_sorted = sorted(word2_c.values())

        word1_key_sorted = set(word1_c.keys())
        word2_key_sorted = set(word2_c.keys())

        return word1_val_sorted == word2_val_sorted and word1_key_sorted == word2_key_sorted


if __name__ == '__main__':
    s = Solution()
    print(s.closeStrings(word1 = "abc", word2 = "bca"))
    print(s.closeStrings(word1 = "a", word2 = "aa"))
    print(s.closeStrings(word1 = "cabbba", word2 = "abbccc"))
    print(s.closeStrings(word1="uau", word2="ssx"))


