""" 
    Problem statement:
        Given an array of unique integers, arr, where each integer arr[i] is trictly greater than 1.
        
        We make a binary tree using these integers, for each number bay be used for any number of times. Each non-leaf node's value 
        should be equal to the product of the values of its children.
        
        Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7

        Example 1:
            Input: arr = [2,4]
            Output: 3
            Explanation: We can make these trees: [2], [4], [4, 2, 2]
            
        Example 2:
            Input: arr = [2,4,5,10]
            Output: 7
            Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
            
        Constraints:
            * 1 <= arr.length <= 1000
            * 2 <= arr[i] <= 10^9
            * All the values of arr are unique
            
        Brain Storming:
            * This can be the math problem.
            * Or we can solve this by using Dynamic Programming.
            
            
        Math first:
            * Find the pair of number that their product has in the array
            * We already has the Unique list, so traverse each element, check if it has any factor (other than itself) that present in the map
        
        Comments:
            * A normal recursion is accepted :/
        
        Hints:
            * Use Dynamic Programming for such Recursion problem -> This will give the Optimal O(n*logn) solution
            
"""
from typing import List

MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """ 
            NOTE: Result always plus with the len(arr), a single Node is meet the constraint.
            This is: O(n * log(n)) solution, but very hard to solve ?!!!
        """
        arr.sort()
        
        # Use the set, this is the same with the dict when looking for just the key
        table = set(arr)
        print(f'Table: {table}')
        
        DP = {value: 1 for value in arr}   # This is call the number of binary tree that can formed by using the value at the root node
        
        for num in arr:
            for j in arr:
                
                if j > num ** 0.5:
                    break
                
                if num % j == 0:
                    factor1 = j
                    factor2 = num // j
                    
                    if factor1 in table and factor2 in table:
                        # Ok, we can list all component like this
                        print(f'Found: {factor1} and {factor2}')
                        if factor1 == factor2:
                            DP[num] += DP[factor1] * DP[factor1] 
                        else:
                            DP[num] += DP[factor1] * DP[factor2] * 2
                        
                        DP[num] %= MOD
        
        # This is just the number of 1-Level Binary tree
        return sum(DP.values()) % MOD
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.numFactoredBinaryTrees(arr=[2, 4]))
    print(s.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))  # Expect 7
    print(s.numFactoredBinaryTrees(arr=[18, 3, 6, 2]))  # Expect 12
