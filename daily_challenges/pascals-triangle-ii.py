""" 
    Problem statement:
        Given an integer rowIndex, return the rowIndex_th (0-indexed) row of the Pascal's Triangle.
        In Pascal's Triangle, each number is the sum of the two numbers directly above it as shown:
        Example 1:
            Input: rowIndex = 3
            Output: [1,3,3,1]
            
        Example 2:
            Input: rowIndex = 0
            Output: [1]
            
        Example 3:
            Input: rowIndex = 1
            Output: [1,1]
        
        Constraints:
            * 0 <= rowIndex <= 33
            
        Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space ?
        
        Brain storm:
            * With trivial solution, I will follow the pascal creation rule one by one. PASS
            * Try to Optimize in term of space, this mean we know about the size of the final array
                + Build strategy to update all value inside this. Okey I need 1 more variable as memorization.
                + While picking the pair of value
"""
from typing import List


class Solution:
    def getRow_NotOptimized(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pascal_arr = [[1], [1, 1]]
        
        for i in range(2, rowIndex + 1):
            prev_arr = pascal_arr[-1]
            constructed_arr = [1]
            for j in range(0, len(prev_arr) - 1):
                constructed_arr.append(prev_arr[j] + prev_arr[j + 1])
            constructed_arr.append(1)
            pascal_arr.append(constructed_arr)
        
        return pascal_arr[-1]
    
    
    def getRow(self, rowIndex: int) -> List[int]:
        """ This is the optimized in space solution

        Args:
            rowIndex (int): _description_

        Returns:
            List[int]: _description_
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        # Construct the final array
        rs = [0] * (rowIndex + 1)
        rs[0] = 1
        rs[1] = 1
        
        # For loop like above function to iterative generate the final array
        for i in range(2, rowIndex + 1):
            # Begin of the reconstruction process
            memorize = rs[0]  # Always remember 1 first
            for j in range(0, i-1):
                tmp = rs[j + 1]
                rs[j + 1] = memorize + rs[j + 1]
                memorize = tmp
            rs[i] = 1
        
        return rs
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.getRow(rowIndex=4))
    # print(s.getRow(rowIndex=0))
    # print(s.getRow(rowIndex=1))