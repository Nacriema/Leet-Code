""" 
    Problem statement:
        You are given a string s consisting only of the characters '0' and '1'. 
        In one operation, you can change any '0' to '1' or vice versa.
        The string is called alternating if no two adjacent characters are equal.
        For example, the string "010" is alternating, while the string "0100" is not.
        Return the minimum number of operations needed to make s alternating.

        Example 1:
            Input: s = "0100"
            Output: 1
            Explanation: If you change the last character to '1', s will be "0101", which is alternating.

        Example 2:
            Input: s = "10"
            Output: 0
            Explanation: s is already alternating.

        Example 3:
            Input: s = "1111"
            Output: 2
            Explanation: You need two operations to reach "0101" or "1010".

        Constraints:
            * 1 <= s.length <= 10^4
            * s[i] is either '0' or '1'.

        Hints:
            * Think about the final string will be
"""
class Solution:
    def minOperations(self, s: str) -> int:
        # Construct 2 difference result
        first = "10" * (len(s) // 2)
        second = "01" * (len(s) // 2)
        if len(s) % 2 == 1:
            first += "1"
            second += "0"

        count_first = count_second = 0
        for (a, b, c) in zip(s, first, second):
            if a != b:
                count_first += 1
            if a != c:
                count_second += 1
        return min(count_first, count_second)


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(s = "0100"))
    print(s.minOperations(s = "10"))
    print(s.minOperations(s = "1111"))