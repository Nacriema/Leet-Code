""" 
    Problem Statement:
        URL: https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
        885. Spiral Matrix III
        You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
        You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
        Return an array of coordinates representing the positions of the grid in the order you visited them.

        Example 1:
            Input: rows = 1, cols = 4, rStart = 0, cStart = 0
            Output: [[0,0],[0,1],[0,2],[0,3]]

        Example 2:
            Input: rows = 5, cols = 6, rStart = 1, cStart = 4
            Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

        Constraints:
            * 1 <= rows, cols <= 100
            * 0 <= rStart < rows
            * 0 <= cStart < cols
"""
from typing import List
import time


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        remains = rows * cols
        rs = []
        left, top, right, bottom = cStart, rStart, cStart + 2, rStart + 2
        while remains:
            # 4 level of loops
            for i in range(left, right):
                if 0 <= i < cols and  0 <= top < rows: 
                    rs.append([top, i])
                    remains -= 1
            print(f'Up   : {rs} - left {left}, right {right}')

            for j in range(top + 1, bottom):
                if 0 <= j < rows and  0 <= right - 1 < cols:
                    rs.append([j, right - 1])
                    remains -= 1
            print(f'Right: {rs} - top {top} bottom {bottom}')
            
            for i in range(right - 2, left - 2, -1):
                if 0 <= i < cols and  0 <= bottom - 1 < rows: 
                    rs.append([bottom - 1, i])
                    remains -= 1
            print(f'Down : {rs} - right {right - 1} left {left - 2}')

            for j in range(bottom - 2, top - 1, -1):
                if 0 <= j < rows and  0 <= left - 1 < cols:
                    rs.append([j, left - 1])
                    remains -= 1
            
            print(f'Left : {rs} - bottom {bottom - 2} top {top - 1}')
            print("="*60)
            # time.sleep(1)

            left -= 1
            right += 1
            top -= 1
            bottom += 1
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.spiralMatrixIII(rows = 1, cols = 4, rStart = 0, cStart = 0))
    print(s.spiralMatrixIII(rows = 5, cols = 6, rStart = 1, cStart = 4))  # [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    print(s.spiralMatrixIII(rows = 3, cols = 3, rStart = 0, cStart = 0))  # [[0,0],[0,1],[1,1],[1,0],[0,2],[1,2],[2,2],[2,1],[2,0]]
