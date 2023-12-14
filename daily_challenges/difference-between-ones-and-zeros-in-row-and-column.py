""" 
    Problem statement:  
        You are given a 0-indexed m x n binary matrix grid.
        
        A 0-indexed m x n difference matrix diff is created with the following procedure:
            Let the number of ones in the ith row be onesRowi.
            Let the number of ones in the jth column be onesColj.
            Let the number of zeros in the ith row be zerosRowi.
            Let the number of zeros in the jth column be zerosColj.
            diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
        
        Return the difference matrix diff.

        Example 1:
            Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
            Output: [[0,0,4],[0,0,4],[-2,-2,2]]
            Explanation:
                - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
                - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
                - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
                - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
                - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0 
                - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4 
                - diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
                - diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
                - diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

        Example 2:
            Input: grid = [[1,1,1],[1,1,1]]
            Output: [[5,5,5],[5,5,5]]
            Explanation:
                - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
                - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
                - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
                - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
                - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
                - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5
                
        Constraints:
            * m == grid.length
            * n == grid[i].length
            * 1 <= m, n <= 10^5
            * 1 <= m * n <= 10^5
            * grid[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """ 
            Same approach with Special Problem in a Binary Matrix problem
        """
        m = len(grid)
        n = len(grid[0])
        row_sum = [0] * m  # Number of ones in rows
        col_sum = [0] * n  # Number of ones in rows
        diff = [[0] * n for _ in range(m)]  # Construct the diff matrix
        
        # First loop to get the picture of the array
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_sum[i] += grid[i][j]
                    col_sum[j] += grid[i][j]
                
        # Second loop to calculate the result in diff matrix 
        for i in range(m):
            for j in range(n):
                diff[i][j] = row_sum[i] + col_sum[j] - (n - row_sum[i]) - (m - col_sum[j])
        return diff


if __name__ == '__main__':
    s = Solution()
    print(s.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))
    # print(s.onesMinusZeros(grid = [[1,1,1],[1,1,1]]))