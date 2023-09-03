"""
    Problem Statement: 
        Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses
        to make the input string valid

        Returns a list of unique strings that are valid with the MINIMUM number of removals. You may return the answer in any order.

    Example 1:
        Input: s = "()())()"
        Output: ["(())()","()()()"]        
    
    Example 2:
        Input: s = "(a)())()"
        Output: ["(a())()","(a)()()"]

    Example 3: 
        Input: s = ")("
        Output: [""] 

    Constraints:
        * 1 <= s.length <= 25
        * s consists of lowercase English letters and parentheses '(' and ')'.
        * There will be at most 20 parentheses in s.

    Use RECURSION, I see that the constrains not strict !
    Hint: 
        1. Since we do not know which brackets can be removed, we try all the options! We can use recursion.
        2. In the recursion, for each bracket, we can either use it or remove it.
        3. Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.
        4. We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.

    NOTE: My solution is too BAD :(        
"""
from typing import List
from collections import deque
import copy


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
            Okay, I implemented the transaction ways of doing the 
        """

        # Get the frequency
        freq = dict()
        for _ in s:
            freq[_] = freq.get(_, 0) + 1
        print(f'Frequency array: {freq}')

        n = len(s)
        store = [("", deque(maxlen=n), 0, freq.get(')', 0))]
        index = 0
        result = []
        
        while index < n:
            # 1. Get the current characters
            char = s[index]
            temp = []

            # 2. Handle for current state (current character in the string)
            while len(store):
                curr_string, curr_stack, removed_parentheses, remain_close = store.pop()
                
                # Stop ciriteria
                if index == n - 1:
                    if len(curr_stack) == 0:
                        if char not in ('(', ')'):
                            result.append((curr_string + char, removed_parentheses))
                        else:
                            result.append((curr_string, removed_parentheses + 1))
                    elif len(curr_stack) == 1 and curr_stack[-1] == '(' and char == ')':
                        result.append((curr_string + char, removed_parentheses))
                    else:
                        # Skip for others
                        continue
                else:
                    """
                    When we are in progress ...
                    When we got '(', we have 2 options:
                        - Append this into the stack 
                        - Not use this

                    Check for the eliminated cases:
                    When we got ')':
                        - If the stack size == 0 => force to skip that character
                        - If the stack size > 0 => pop a single '(' out of the stack  
                    
                    When we got normal:
                        - Use this
                    """
                    if char == '(':
                        # 1. Use this char, when the len of current stack is greater than the remain close
                        if len(curr_stack) < remain_close:
                            new_stack = copy.deepcopy(curr_stack)
                            new_stack.append(char)
                            temp.append((curr_string + char, new_stack, removed_parentheses, remain_close))
                        
                        # 2. Not use this char
                        temp.append((curr_string, copy.deepcopy(curr_stack), removed_parentheses + 1, remain_close))

                    elif char == ')':
                        if len(curr_stack) == 0:
                            temp.append((curr_string, copy.deepcopy(curr_stack), removed_parentheses + 1, remain_close - 1))
                        else:
                            # 1. Use this char ) 
                            new_stack = copy.deepcopy(curr_stack)
                            new_stack.pop()
                            temp.append((curr_string + char, new_stack, removed_parentheses, remain_close - 1))

                            # 2. Ignore this char )
                            temp.append((curr_string, copy.deepcopy(curr_stack), removed_parentheses + 1, remain_close - 1))
                    else:
                        temp.append((curr_string + char, copy.deepcopy(curr_stack), removed_parentheses, remain_close))

            store.extend(temp)
            index += 1
        
        result = set(result)
        result = sorted(result, key=lambda x: x[1], reverse=False)
        string, count = result[0]
        rs = [string]
        for string, count_ in result[1: ]:
            if count_ == count:
                rs.append(string)
            else: break
        return rs


if __name__ == '__main__':
    s = Solution()
    # print(s.removeInvalidParentheses(s = "()())()"))  # ["(())()","()()()"]
    # print(s.removeInvalidParentheses(s = "(a)())()"))
    # print(s.removeInvalidParentheses(s= ")("))
    # print(s.removeInvalidParentheses(s="x("))
    print(s.removeInvalidParentheses(s="((((((((((((((((((((aaaaa"))  # TLE Case :'(((

