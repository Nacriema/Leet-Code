# Link: https://leetcode.com/problems/reorganize-string/

"""
Given a string s, rearrange the characters of s so that any 2 adjacent characters are not the same.

Return ANY POSSIBLE rearrangement of s or just return "" if not possible.

This problem need Greedy thinking, we try to simplify the problem by mapping it from the original domain to the 
other domain that we can solved

Here, my strategy is "Use 2 characters with high ocurrence frequency first"

Consider this case: "vvvlo"

Use priority queue to get
"""
from collections import Counter
from queue import PriorityQueue


class Solution:
    def reorganizeString_dict(self, s):
        """
            :type s: str
            :rtype: str
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Sort the freq dict by the value
        freq_sorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        
        # Pick 2 most occurence character to form the string, keep track the latest character that appended to the result_string
        out_string = ''
        last_append_char = None

        while len(freq_sorted):
            freq_sorted = dict(sorted(freq_sorted.items(), key=lambda item: item[1], reverse=True))
            freq_sorted_cpy = freq_sorted.copy()
            print(f'Update freq_sorted: {freq_sorted}, out_string: {out_string}')
            
            if len(freq_sorted_cpy) == 1:
                char = next(iter(freq_sorted_cpy))
                if char != last_append_char and freq_sorted_cpy[char] == 1:
                    out_string += str(char)
                    return out_string
                return ""
            
            else:
                # Pick the most 2 most frequent characters
                print(f'Get 2 most character, {freq_sorted_cpy}')
                curr_index = 0
                first_char = second_char = None
                
                for char, occurence in freq_sorted_cpy.items():
                    if curr_index == 2:
                        break
                    else:
                        if curr_index == 0:
                            first_char = char
                        else:
                            second_char = char
                        
                        # Check for occurence, If 
                        if occurence > 1:
                            freq_sorted[char] = occurence - 1
                        else:
                            freq_sorted.pop(char)
                        curr_index += 1
                print(f'First char {first_char}, Second char {second_char}, Outstring: {out_string}, Last char: {last_append_char}')
                if last_append_char != first_char:
                    out_string += f'{first_char}{second_char}'
                    last_append_char = second_char
                    print(f'Last append char: {last_append_char}')
                else:
                    return ""
        return out_string


    def reorganizeString_priority_queue(self, s: str) -> str:
        """
            :type s: str
            :rtype: str
        """
        freq = Counter(s)
        priority_queue = PriorityQueue()

        for char, count in freq.items():
            priority_queue.put((-count, char))
        
        out_string = ''
        last_append_char = None
        
        while priority_queue.qsize():
            queue_size = priority_queue.qsize()

            if queue_size == 1:
                neg_freq, char = priority_queue.get()
                if char != last_append_char and neg_freq == -1:
                    out_string += str(char)
                    return out_string
                return ""
            else:
                # Pick 2 most frequent characters
                first_neg_freq, first_char = priority_queue.get()
                second_neg_freq, second_char = priority_queue.get()
                print(f'First char {first_char}, Second char {second_char}, Outstring: {out_string}, Last char: {last_append_char}')

                if last_append_char != first_char:
                    out_string += f'{first_char}{second_char}'
                    last_append_char = second_char
                    print(f'Last append char: {last_append_char}')

                    # Put back the items into the priority_queue, if they can be used
                    if first_neg_freq < -1:
                        priority_queue.put((first_neg_freq + 1, first_char))
                    if second_neg_freq < -1:
                        priority_queue.put((second_neg_freq + 1, second_char))
                
                else:
                    return ""
        return out_string


if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString_dict(s='ogccckcwmbmxtsbmozli'))
    print(s.reorganizeString_priority_queue(s='vvvlo'))
