""" 
    Problem Statement:
        URL: https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-interview-150
        54. Spiral Matrix
        Given an m x n matrix, return all elements of the matrix in spiral order.

        Example 1:
            Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [1,2,3,6,9,8,7,4,5]

        Example 2:
            Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
            Output: [1,2,3,4,8,12,11,10,9,5,6,7]

        Constraints:
            * m == matrix.length
            * n == matrix[i].length
            * 1 <= m, n <= 10
            * -100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        rs = []
        if rows == 1:
            return matrix[0]
        if cols == 1:
            for i in range(0, rows):
                rs.append(matrix[i][0])
            return rs    
        # Initial values
        left, right = -1, cols
        top, bottom = -1, rows
        while left + 1 <= right - 1 and top + 1 <= bottom - 1:
            left, right = left + 1, right - 1
            top, bottom = top + 1, bottom - 1
            
            # Print 4 borders defined by top-left and bottom-right
            for i in range(left, right + 1):
                rs.append(matrix[top][i])
            
            for i in range(top + 1, bottom + 1):
                rs.append(matrix[i][right])
            
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    rs.append(matrix[bottom][i])
            
            if left < right:
                for i in range(bottom - 1, top, -1):
                    rs.append(matrix[i][left])
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))