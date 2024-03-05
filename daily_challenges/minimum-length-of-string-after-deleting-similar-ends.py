""" 
Problem statement:
    Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
        1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        3. The prefix and the suffix should not intersect at any index.
        4. The characters from the prefix and suffix MUST be the same.
        5. Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any number of times (possibly zero times).

    Example 1:
        Input: s = "ca"
        Output: 2
        Explanation: You can't remove any characters, so the string stays as is.

    Example 2:
        Input: s = "cabaabac"
        Output: 0
        Explanation: An optimal sequence of operations is:
            - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
            - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
            - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
            - Take prefix = "a" and suffix = "a" and remove them, s = "".

    Example 3:
        Input: s = "aabccabba"
        Output: 3
        Explanation: An optimal sequence of operations is:
            - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
            - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

    Constraints:
        * 1 <= s.length <= 10^5
        * s only consists of characters 'a', 'b', and 'c'.
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        """
            May be 2 pointers problem
        """
        start_idx = 0
        end_idx = len(s) - 1
        
        start_continuous = 0
        end_continuous = 0
        
        # Finding the maximum consercutive character and their indexes
        while True:
            print(f'Start index: {start_idx}, End index: {end_idx}, Start continuous: {start_continuous}, End continuous: {end_continuous}')
            print(f'Remaining string: {s[start_idx - start_continuous: end_idx - end_continuous + 1]}')
            if len(s[start_idx - start_continuous: end_idx - end_continuous + 1]) == 1: return 1  # This is the remaining string
            while (start_idx < len(s) - 1 and s[start_idx] == s[start_idx + 1]):
                start_idx += 1
                start_continuous += 1
            
            while (end_idx > 0 and s[end_idx] == s[end_idx - 1]):
                end_idx -= 1
                end_continuous += 1
            
            # Check for the start and end
            if s[start_idx] != s[end_idx]:
                # TODO: Roll back to the start position by continuous frames from start and end to give the best match
                return (end_idx + end_continuous - (start_idx - start_continuous) + 1)
            
            elif start_idx > end_idx:
                # Overlap means that the remains string is 0
                return 0
            else:
                # Case we found the matched between start and end
                start_idx += 1
                end_idx -= 1
                start_continuous = 0
                end_continuous = 0


if __name__ == '__main__':
    s = Solution()
    # print(s.minimumLength(s = "ca"))
    # print(s.minimumLength(s = "cabaabac"))
    # print(s.minimumLength(s = "aabccabba"))
    print(s.minimumLength(s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))  # Expected: 1
    print(s.minimumLength(s = "bbbbbbbbbbbbbbbbbbb"))