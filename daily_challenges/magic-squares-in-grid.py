""" 
    Problem Statement:
        URL: https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09
        840. Magic Squares In Grid
        A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
        Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there ?
        Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

        Example 1:
            Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
            Output: 1
            Explanation: 
                The following subgrid is a 3 x 3 magic square:
                while this one is not:
                In total, there is only one magic square inside the given grid.

        Example 2:
            Input: grid = [[8]]
            Output: 0

        Constraints:
            * row == grid.length
            * col == grid[i].length
            * 1 <= row, col <= 10
            * 0 <= grid[i][j] <= 15
"""
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        count = 0
        for i in range(1, nrows - 1):
            for j in range(1, ncols - 1):
                # print(f'i: {i}, j: {j}')
                # Check for 4 neigh bor
                if grid[i][j] != 5:
                    continue
                if grid[i - 1][j - 1] + grid[i + 1][j + 1] == 10 and \
                   grid[i - 1][j] + grid[i + 1][j] == 10 and \
                   grid[i - 1][j + 1] + grid[i + 1][j - 1] == 10 and \
                   grid[i][j + 1] + grid[i][j - 1] == 10 and \
                   grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] == 15 and \
                   grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] == 15 and \
                   grid[i - 1][j - 1] + grid[i][j - 1] + grid[i + 1][j - 1] == 15 and \
                   grid[i - 1][j + 1] + grid[i][j + 1] + grid[i + 1][j + 1] == 15 and\
                   set([
                      grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],\
                      grid[i][j - 1], grid[i][j], grid[i][j + 1],\
                      grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                   ]) == set(range(1, 10)):
                   count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
    print(s.numMagicSquaresInside(grid = [[8]]))
