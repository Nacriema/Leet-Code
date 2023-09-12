"""
    Problem Statement:
        A string s is called good if there are no two difference characters in s that have the same frequency.
        Given a string s, return the minimum number of characters you need to delete to make s good.
        The frequency of a character in a string is the number of times it appears in the string. For example, 
        in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
        
    Example 1:
        Input: s = "aab"
        Output: 0
        Explanation: s is already good.
    
    Example 2:
        Input: s = "aaabbbcc"
        Output: 2
        Explanation: You can delete two 'b's resulting in the good string "aaabcc".
        Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
            
    Example 3:
        Input: s = "ceabaacb"
        Output: 2
        Explanation: You can delete both 'c's resulting in the good string "eabaab".
        Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored)
        
    Constrains:
        * 1 <= s.length <= 10^5
        * s contains only lowercase English letters
        
    Hint:
        * As we can only delete characters, if we have multiple characters having the same frequency, we must decrease all the frequencies of them, except one.
        * Sort the alphabet characters by their frequencies non-increasingly.
        * Iterate on the alphabet characters, keep decreasing the frequency of the current character until it reaches a value that has not appeared before.

"""
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        """
        # Construct the occuppancy table
        count = 0
        
        # 1. Get the frequency dictionary, Use collections Counter is much faster than use the dict().get
        freq = dict(Counter(s))
        
        print(f'Frequency character: {freq}')
        
        # 2. Sort the freq dictionary by on inscreasingly
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        print(f'Sorted frequency: {freq}')
        
        freq_vals = list(freq.values())
        
        last = None        
        # 3. For each
        for k, v in freq.items():
            # Track by the unseen list
            if last is None or v != last:
                # Found the unseen
                print(f'First time we see: {v}')
                last = v
            else:
                last = v
                while v > 0:
                    # Decrease v value until we find a new value and this value is not in freq_vals
                    if v in freq_vals:
                        count += 1
                        v -= 1
                    else:
                        print(f'Found new value: {v}')
                        freq_vals.append(v)
                        break
        return count
        
    

if __name__ == '__main__':
    s = Solution()
    # print(s.minDeletions(s="aab"))
    # print(s.minDeletions(s="aaabbbcc"))
    # print(s.minDeletions(s="ceabaacb"))
    print(s.minDeletions(s="abcabc"))

