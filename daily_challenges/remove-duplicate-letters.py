"""
    Problem Statement: 
        Given a string s, remove duplicate letters so that every letter appears once 
        and only once. You must make sure your result is the smallest in lexicographical 
        order among all possible result.
        
    Example 1:
        Input: s = "bcabc"
        Output: "abc" 
        
    Example 2:
        Input: s = "cbacdcbc"
        utput: "acdb"
        
        
    Constraints:
        * 1 <= s.length <= 10^4
        * s consists of lowercase English letters.
        
    Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

    Hint: Greedily try to add one missing character. How to check if adding some character will not cause problems ? 
          Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

"""
class Solution:
    def removeDuplicateLetters_NotPass(self, s: str) -> str:
        """
            Remove letters in string s so that:
                * Each letter appeears once and only once
                * REMAIN the order of letter
                * Smallest lexicographical order
        """
        def add(current_str, current_state , new_char, position):
            # Decide where to put inside the current state based on the position
            insert_index = find_index(arr=current_state, K=position)
            current_str = current_str[:insert_index] + new_char + current_str[insert_index:]
            new_state = current_state.copy()
            new_state.insert(insert_index, position)
            return current_str, new_state 


        # Function to find insert position of K
        def find_index(arr, K):
            # Lower and upper bounds
            start = 0
            end = len(arr) - 1
            # Traverse the search space
            while start<= end:
                mid =(start + end)//2
                if arr[mid] == K:
                    return mid
                elif arr[mid] < K:
                    start = mid + 1
                else:
                    end = mid-1
            # Return the insert position
            return end + 1
        
        # For loop through the string s, generate the map
        # {"character": [positions]}
        table_ = dict()
        for id, char in enumerate(s):
            table_[char] = table_.get(char, [])
            table_[char].append(id)
            print(table_[char])
            
        print(f'Table map: {table_}')
        
        # Construct lexicographic order, the fact that if I'm doing this way I have the time complexity O(26 * 26!) Too big !!!
        table = sorted(table_.items(), key=lambda x: x[0])
        print(f'Sorted table: {table}')
        
        target_len = len(table)
        print(f'Targeted length: {target_len}')
        
        # Reconstruct the string in the Greedy way, for each string, give it a list of index
        # https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/
        # This problem MUST be in the DEPTH-FIRST-SEARCH style
        my_stack = [('', [])]  # The more to the end of stack -> The more the high priority
        
        while len(my_stack) > 0:
            # Special, when we handle at state == len(table) - 1
            # Get all item that has this length: 
            
            # Handle for that stage
            char, possible_positions = table[len(my_stack[-1][1])]
            print(f'Check char: {char}, with possible positions: {possible_positions}')
            
            final_result_list = []
            
            while len(my_stack) and len(my_stack[-1][1]) == (len(table) - 1):
                # Check the final inserted index
                current = my_stack.pop()
                print(f'Process final for str: {current[0]}, state: {current[1]}, and new incoming char: {char}')
                
                # Find the inserted, track for the largest index can insert
                for position in table_.get(char):
                    print(f'Final str: {current[0]}, state: {current[1]}, new char:{char}, position: {position}')
                    new_str, new_state = add(current_str=current[0], current_state=current[1], new_char=char, position=position)
                    
                    print(f'Final new str: {new_str}')
                    final_result_list.append(new_str)
                    print(f'Final result list: {final_result_list}')
                    
                    print(f'My stack: {my_stack}')
            
            
            if len(final_result_list):
                print(f"Final result list: {final_result_list}")
                return sorted(final_result_list)[0]
            
            current = my_stack.pop()    # Get the most possible correct answer
            curr_str, curr_state = current
            print(f'We are at stage: {len(curr_state)}')
            
            
            for position in possible_positions:
                if curr_str == '':
                    my_stack.append((char, [possible_positions[0]]))
                else:
                    print(f'Handle for non empty string: {curr_str}, with state: {curr_state}')
                    new_str, new_state = add(current_str=curr_str, current_state=curr_state, new_char=char, position=position)
                    print(f'New string: {new_str}, New State: {new_state}')
                    my_stack.append((new_str, new_state))
            print(f'My stack: {my_stack}')
            
        #     for char, indexes in table:
        # print(f'Char: {char}, Indexes: {indexes}')
        
        
        # for index in indexes:
        #     print(f"Index: {index}")
        #     # At this time we have the current value
        #     curr_str, curr_state = current
            
        #     # Try to add the current character and index of it into the curr_str and curr_state
        #     if curr_str == '' and curr_state == []:
        #         my_stack.append((char, [index]))
            
        #     print(f'My stack: {my_stack}')
                
        
        
        
        # # 1. Convert to set
        # tmp = set(s)
        # print(f'Set from s: {tmp}')
        
        # # 2. Sort the set
        # tmp = sorted(tmp)
        # # 3. Join the string
        # return "".join(tmp)

    
    def removeDuplicateLetters(self, s: str) -> str: 
        """"""
        stack = []
        seen = set() 
        last_occ = {c: i for i, c in enumerate(s)}

        print(f'Lass occ: {last_occ}')
        for idx, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and idx < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        print(f'Stack: {stack}')


if __name__ == '__main__':
    s = Solution()
    # print(s.removeDuplicateLetters(s="bcabc"))
    # print(s.removeDuplicateLetters(s="cbacdcbc"))
    # print(s.removeDuplicateLetters(s="cdadabcc"))   # Expect: adbc
    print(s.removeDuplicateLetters(s="leetcode"))
        
    # print(permute(lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
    # val = 0b111
    # print('{:b}'.format(set_bit(val, bit=4)))   
    
    # print(find_index(arr=[2], K=6))