""" 
    Problem statement:
        Given an m x n binary matrix mat, return the number of special positions in mat.
        A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
        
        Example 1:
            Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
            Output: 1
            Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
            
        Example 2:
            Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
            Output: 3
            Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
            
        Constraints:
            * m == mat.length
            * n == mat[i].length
            * 1 <= m, n <= 100
            * mat[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """ 
            This can be optimized more by using break
        """
        # 1. Get the sum for each row and col
        m = len(mat)
        n = len(mat[0])
        row_sum = [0] * m
        col_sum = [0] * n
        one_pos = dict() # type: dict
        count = 0
        
        for i in range(m):
            s = 0
            for j in range(n):
                s += mat[i][j]
                col_sum[j] += mat[i][j]
                if mat[i][j] == 1:
                    one_pos.update({(i, j): 1})
            print(f'Sum of row {i}: {s}')
            row_sum[i] = s   
        print(f'Row sum: {row_sum}')
        print(f'Col sum: {col_sum}')      
        print(f'One pos: {one_pos}')
        for (i, j) in one_pos.keys():
            if row_sum[i] == col_sum[j] == 1:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]]))
    print(s.numSpecial(mat = [[1,0,0],[0,1,0],[0,0,1]]))