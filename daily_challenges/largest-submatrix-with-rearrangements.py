""" 
    Problem statement:
        You are given a binary matrix matrix of size m x n, 
        and you are allowed to rearrange the columns of the matrix in any order.
        Return the area of the largest submatrix within matrix where every element of 
        the submatrix is 1 after reordering the columns optimally.

        Example 1:
            Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
            Output: 4
            Explanation: 
                You can rearrange the columns as shown above.
                The largest submatrix of 1s, in bold, has an area of 4.

        Example 2:
            Input: matrix = [[1,0,1,0,1]]
            Output: 3
            Explanation: 
                You can rearrange the columns as shown above.
                The largest submatrix of 1s, in bold, has an area of 3.

        Example 3:
            Input: matrix = [[1,1,0],[1,0,1]]
            Output: 2
            Explanation: Notice that you must rearrange entire columns, 
            and there is no way to make a submatrix of 1s larger than an area of 2.

        Constraints:
            * m == matrix.length
            * n == matrix[i].length
            * 1 <= m * n <= 10^5
            * matrix[i][j] is either 0 or 1.
"""
from typing import List


class Solution(object):
    def largestSubmatrix(self, matrix):
        def printmatrix(m):
            rows, cols = len(m), len(m[0])
            for i in range(rows):
                for j in range(cols):
                    print(f'{m[i][j]} ', end="")
                print()
            print('=' * 50)
        
        rows, cols = len(matrix), len(matrix[0])
        
        printmatrix(matrix)
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
        
        printmatrix(matrix)
        ans = 0
        
        for row in matrix:
            row.sort(reverse=True)
            for j in range(cols):
                ans = max(ans, row[j] * (j + 1))        
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.largestSubmatrix(matrix = [[0,0,1],[1,1,1],[1,0,1]]))
    # print(s.largestSubmatrix(matrix = [[1,0,1],[0,1,1],[1,0,1]]))

    # print(s.largestSubmatrix(matrix = [[1,0,1,0,1]]))
    # print(s.largestSubmatrix(matrix = [[1,1,0],[1,0,1]]))