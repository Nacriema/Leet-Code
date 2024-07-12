""" 
    Problem Statement:
        URL: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2024-07-11
        1190. Reverse Substrings Between Each Pair of Parentheses
        You are given a string s that consists of lower case English letters and brackets.
        Reverse the strings in each pair of matching parentheses, starting from the innermost one.

        Your result should not contain any brackets.
        Example 1:
            Input: s = "(abcd)"
            Output: "dcba"

        Example 2:
            Input: s = "(u(love)i)"
            Output: "iloveu"
            Explanation: The substring "love" is reversed first, then the whole string is reversed.

        Example 3:
            Input: s = "(ed(et(oc))el)"
            Output: "leetcode"
            Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

        Constraints:
            * 1 <= s.length <= 2000
            * s only contains lower case English characters and parentheses.
            * It is guaranteed that all parentheses are balanced.
"""
from collections import defaultdict


class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Loop and push the item to the stack, do processing right after we got a ) (finihed a level)
        word, level = '', 0
        mapping_level = defaultdict(list)

        for c in s:
            if c == '(':
                mapping_level[level].append(word)
                level += 1
                word = ''
                pass
            elif c == ')':
                # Performing reverse ...
                print(f'Reverse ...')
                mapping_level[level].append(word)
                reconstructed_word = ''.join(mapping_level[level])[::-1]
                mapping_level[level - 1].append(reconstructed_word)
                del mapping_level[level]
                print(f'Mapping level: {mapping_level}')
                level -= 1
                word = ''
                pass 
            else:
                word += c
        
        if len(word):
            mapping_level[level].append(word)
        return ''.join(mapping_level[0])


if __name__ == '__main__':
    s = Solution()
    # print(s.reverseParentheses(s = "(abcd)"))
    # print(s.reverseParentheses(s = "(u(love)i)"))
    print(s.reverseParentheses(s = "(ed(et(oc))el)"))
    print(s.reverseParentheses(s = "a(bcdefghijkl(mno)p)q"))