""" 
    Problem Statement:
        Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty
        
        Example 1:
            Input: s = "ab#c", t = "ad#c"
            Output: true
            Explanation: Both s and t become "ac".
            
        Example 2:
            Input: s = "ab##", t = "c#d#"
            Output: true
            Explanation: Both s and t become "".
            
        Example 3:
            Input: s = "a#c", t = "b"
            Output: false
            Explanation: s becomes "c" while t becomes "b".

        Constraints:
            * 1 <= s.length, t.length <= 200
            * s and t only contain lowercase letters and '#' characters.
        
        Follow up: Can you solve it in O(n) time and O(1) space?

        Currently: 
            * The Naive solution is like 2 * O(n) time, and space is 2 * O(n)
        
        Brain Storming:
            * O(n) time mean one for loop
            * O(1) space mean the memory is CONSTANT for all cases
            * 
"""

class Solution:
    def backspaceCompare_Naive(self, s: str, t: str) -> bool:
        """ Naive solution first, we construct the final string for both s and t

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        def process(inp):
            queue = []
            for char in inp:
                if char != '#':
                    queue.append(char)
                else:
                    if len(queue):
                        queue.pop()
                    continue
            return ''.join(queue)
        
        s = process(s)
        t = process(t)
        print(f'Final s: {s}, t: {t}')
        return s == t
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ O(n) time and O(1) space solution: How can I do this ???

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        pass
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare(s = "ab#c", t = "ad#c"))
    print(s.backspaceCompare(s = "ab##", t = "c#d#"))
    print(s.backspaceCompare(s = "a#c", t = "b"))