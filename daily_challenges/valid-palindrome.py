""" 
    Problem statement:
        A pharse is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
        non-alphanumeric characters, it read the same forward and backward. Alphanumeric characters include letters 
        and numbers.

        Given a a string s, return True if it is a palindrome, or False otherwise

        Example 1:
            Input: s = "A man, a plan, a canal: Panama"
            Output: true
            Explanation: "amanaplanacanalpanama" is a palindrome.

        Example 2:
            Input: s = "race a car"
            Output: false
            Explanation: "raceacar" is not a palindrome.

        Example 3: 
            Input: s = " "
            Output: true
            Explanation: s is an empty string "" after removing non-alphanumeric characters.
            Since an empty string reads the same forward and backward, it is a palindrome.
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", '', s).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(s.isPalindrome(s="race a car"))
    print(s.isPalindrome(s=" "))
    print(s.isPalindrome(s="ab_a"))

