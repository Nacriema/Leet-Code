"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.



Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".


Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 109
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        my_stack = []
        word = ""
        for char in s:
            if char.isdigit():
                if len(my_stack) == 0:
                    my_stack.append((word, len(word), int(char)))
                else:
                    if len(word):
                        my_stack.append((word, my_stack[-1][1] * my_stack[-1][2] + len(word), int(char)))
                    else:
                        my_stack.append((my_stack[-1][0], my_stack[-1][1] * my_stack[-1][2], int(char)))
                word = ""
            else:
                word += char
        
        if len(my_stack) == 0:
            my_stack.append((word, len(word), 1))

        print(f'My stack: {my_stack}')

        # Process with my_stack 
        while len(my_stack):
            last_word, total_length, repeat = my_stack.pop()
            k %= total_length
            print(f'Current state: {my_stack}, K: {k}, Total length: {total_length}, Last word: {last_word}')
            if k > total_length - len(last_word):
                rs = k - (total_length - len(last_word)) - 1
                return last_word[rs]
            elif k == total_length - len(last_word):
                if len(my_stack):
                    return my_stack[-1][0]
                else:
                    return last_word[k-1]
            elif k == 0: 
                return last_word[-1]
            else:
                continue

if __name__ == '__main__':
    s = Solution()
    # print(s.decodeAtIndex(s = "leet2code3", k = 10))
    # print(s.decodeAtIndex(s="ha22", k=5))
    # print(s.decodeAtIndex(s="a2345678999999999999999", k = 1))
    # print(s.decodeAtIndex(s="abc", k=1))
    # print(s.decodeAtIndex(s="a2b3c4d5e6f7g8h9", k=3))
    # print(s.decodeAtIndex(s="abc", k=3))
    # print(s.decodeAtIndex(s="a2b3c4d5e6f7g8h9", k=9))
    print(s.decodeAtIndex(s="a2b3c4d5e6f7g8h9", k=3))  # Expect b