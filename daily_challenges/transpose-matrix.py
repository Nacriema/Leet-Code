""" 
    Problem statement:
        Given a 2D integer array matrix, return the transpose of matrix.
        The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

        Example 1:
            Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [[1,4,7],[2,5,8],[3,6,9]]

        Example 2:
            Input: matrix = [[1,2,3],[4,5,6]]
            Output: [[1,4],[2,5],[3,6]]

        Constraints:
            * m == matrix.length
            * n == matrix[i].length
            * 1 <= m, n <= 1000
            * 1 <= m * n <= 10^5
            * -10^9 <= matrix[i][j] <= 10^9
"""
from typing import List


class Solution:
    def printMat(self, mat):
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                print(mat[row][col], end=' ')
            print()

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Construct the 2D empty maxtrix
        m = len(matrix)
        n = len(matrix[0])        
        transposed_mat = [[0] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                transposed_mat[col][row] = matrix[row][col]
        return transposed_mat


if __name__ == '__main__':
    s = Solution()
    print(s.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(s.transpose(matrix = [[1,2,3],[4,5,6]]))
    