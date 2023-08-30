"""
    Problem Set:
        You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

        For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7]
        
        Return the minimum number of operations to make an array that is sorted in non-decreasing order. Ex [1, 2, 3] is non decreasing order
        
    Example 1:

        Input: nums = [3,9,3]
        Output: 2
        Explanation: Here are the steps to sort the array in non-decreasing order:
            - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
            - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
            There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
            
    Example 2:
    
        Input: nums = [1,2,3,4,5]
        Output: 0
        Explanation: The array is already in non-decreasing order. Therefore, we return 0.
        
    Constrains:
        * 1 <= nums.length <= 105
        * 1 <= nums[i] <= 109
        
    Hint:
        1. It is optimal to never make an operation to the last element of the array, so skip this element
            Ex. [1, 2, 5]; [4, 5, 3]
        2. For loop from the 2nd last value and perform the check

"""
from typing import List


class Solution:
    def minimumReplacement_display_first_attempt(self, nums: List[int]) -> int:
        nb_operations = 0
        
        if len(nums) == 1:
            return nb_operations
        
        i = len(nums) - 2
        
        while i > -1:
            if nums[i] > nums[i + 1]:
                min_val = nums[i] // 2
                max_val = nums[i] - nums[i] // 2
                
                if max_val <= nums[i + 1]:
                    nb_operations += 1
                    nums[i] = max_val
                    nums.insert(i, min_val)
                    i += 1
                else:
                    nb_operations += 1
                    nums[i] = nums[i] - nums[i+1]
                    nums.insert(i+1, nums[i+1])
                    i += 1
            i -= 1
        return nums
    
    def minimumReplacement_display_second_attempt(self, nums: List[int]) -> int:
        nb_operators = 0
        n = len(nums)
        
        # Try to display the result
        reconstruct_nums = [nums[-1]]
        
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                reconstruct_nums = [nums[i]] + reconstruct_nums
                continue
            
            # Minimun elements that we can break from nums[i]
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            smallest_elem = nums[i] // num_elements
            
            # print(f'Num element: {num_elements}, Smallest element: {smallest_elem}, Nuber: {nums[i]}')
            
            # Form the array that demonstrate the break of nums[i]
            break_arr = [smallest_elem] + [(nums[i] - smallest_elem) // (num_elements - 1)] * (num_elements - 1)
            reconstruct_nums = break_arr + reconstruct_nums
            nums[i] = nums[i] // num_elements
        
        return reconstruct_nums
    
    def minimumReplacement(self, nums: List[int]) -> int:
        """
            Implement solution here
            
            This consider as Greedy Approach
            
            Non-decreasing order, example: [1, 2, 5]; [3, 3, 3, 3]
            
            For loop from the 2nd last value of nums List and perform so that:  [..., prev_num, num, aft_num, ...]
                - The current number to break (num = num1 + num2) 
                - Due to non decreasing order so:
                    - Let's choose num2 = aft_num
        """
        nb_operators = 0
        n = len(nums)

        # Start from the second last element, as the last one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue
            
            # Minimun elements that we can break from nums[i]
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            
            # We have numElements - 1 operators
            nb_operators += num_elements - 1

            # Maximize nums[i] after replacement.
            print(f'Replace: {nums[i]} with {nums[i] // num_elements}')
            
            # Replace the nums[i] with the minimal value that we can divide
            nums[i] = nums[i] // num_elements
        
        return nb_operators
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.minimumReplacement(nums=[3, 9, 3]))
    # print(s.minimumReplacement(nums=[1, 2, 3, 4, 5]))
    # print(s.minimumReplacement(nums=[2, 10, 20, 19, 1]))  # Expect: 47
    # print(s.minimumReplacement(nums=[12, 9, 7, 6, 17, 19, 21]))  # Expect: 6
    # print(s.minimumReplacement_display(nums=[12, 9, 7, 6, 17, 19, 21]))  # Expect: 6
    
    
    
    # print(s.minimumReplacement(nums=[3, 11, 4]))
    
    # print(s.minimumReplacement_display(nums=[10, 2, 6, 19, 17, 3]))
    # print(s.minimumReplacement_display(nums=[10, 2, 19, 2]))
    
    
    """
        Some cases like [7, 3] => [1, 3, 3] (Small at the begin) or [2, 2, 3] (Better)
    
    """
    
    # print(s.minimumReplacement_display(nums=[2, 1, 4, 6, 7, 3, 4]))
    
    # print(s.minimumReplacement(nums=[368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223]))
    
    x = [368,112,2,282,349,127,36,98,371,79,309,221,175,262,224,215,230,250,84,269,384,328,118,97,17,105,342,344,242,160,394,17,120,335,76,101,260,244,378,375,164,190,320,376,197,398,353,138,362,38,54,172,3,300,264,165,251,24,312,355,237,314,397,101,117,268,36,165,373,269,351,67,263,332,296,13,118,294,159,137,82,288,250,131,354,261,192,111,16,139,261,295,112,121,234,335,256,303,328,242,260,346,22,277,179,223]
    print(sum(x))
    first_attempt = s.minimumReplacement_display_first_attempt(nums=x)
    print(sum(first_attempt))
    second_attempt = s.minimumReplacement_display_second_attempt(nums=x)
    print(sum(second_attempt))