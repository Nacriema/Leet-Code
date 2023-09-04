"""
    Problem Statement: 
        Given a string containing just the characters '(' and ')'
        Return the length of the longest valid (well-formed) parentheses substring

        Example 1:
            Input: s = "(()"
            Output: 2
            Explanation: The longest valid parentheses substring is "()".

        Example 2:
            Input: s = ")()())"
            Output: 4
            Explanation: The longest valid parentheses substring is "()()".

        Example 3: 
            Input: s = ""
            Output: 0
        
    Constrains:
        * 0 <= s.length <= 3 * 10^4
        * s[i] is '(' or ')'


    TODO: Try with some more ideas !!!
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            Implementation here
            Finding the corresponding () in the string and annotate them as 1
            This is not the Optimal solution so far :<
        """
        mask = [0] * len(s)
        my_stack = deque(maxlen=len(s))

        for i, char in enumerate(s):
            if char == '(':
                my_stack.append(i)
            if char == ')':
                if len(my_stack):
                    mask[i] = 1
                    mask[my_stack.pop()] = 1
                else:
                    continue
        
        # Finding longest 1's in the 0, 1 array
        longest = 0
        tmp = 0
        for i in mask:
            if i == 1: tmp += 1
            else: tmp = 0
            longest = max(longest, tmp)
        # print(f'Longest: {longest}')
        print(mask)
        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses(s="(()"))  # Exepected: 2
    print(s.longestValidParentheses(s=")()())")) # Expected: 4
    print(s.longestValidParentheses(s=""))  # Expected: 0
    print(s.longestValidParentheses(s=")"))  # Expected: 0
    print(s.longestValidParentheses(s="(" * 10 + ")" * 9))  # Expected: 18
    print(s.longestValidParentheses(s="())"))  # Expected: 2
    print(s.longestValidParentheses(s="()(()"))  # Expect: 2
    print(s.longestValidParentheses(s="((()))())"))  # Expected: 8
    print(s.longestValidParentheses(s=")()())()()("))  # Expected: 4
    print(s.longestValidParentheses(s="(()(((()"))  # Expected: 2  # THIS IS HARD CASE :(((
