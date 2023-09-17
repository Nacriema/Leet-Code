"""
    Problem Statement: 
        You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size 
        rows x columns, where heights[row][col] represent the height of cell (row, col). You are 
        situated in the top-left cell, (0, 0) and you hope to travel to the bottom-right cell, 
        (rows-1, columns-1). You can move up, down, left, right and you wish to find a route that 
        requires the minimum effort

        A route's effort is the maximum absolute difference in heights between two consecutive cells of 
        the route.

        Return the minimum effort required to travel from the top-left cell to the bottom-right cell

    Example 1:
        Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
        Output: 2
        Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
            This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.       

    Example 2:
        Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
        Output: 1
        Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
    
    Example 3: 
        Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        Output: 0
        Explanation: This route does not require any effort.

    Constrains:
        * rows == heights.length 
        * columns == heighs[j].length
        * 1 <= rows, columns <= 100
        * 1 <= heights[i][j] <= 10^6

    
    Idea: Use Dijkstra’s Algorithm
        * Create the sptSet (shortest path tree) set that keeps track of verticies included in the shortest path. Initially this set is empty
        * Assign a distance value to all vericies in the input graphs. Initialize distance values as INFINITE
"""
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        """
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.minimumEffortPath(heights=[[1,2,2],[3,8,2],[5,3,5]]))
    print(s.minimumEffortPath(heights=[[1,2,3],[3,8,4],[5,3,5]]))
    print(s.minimumEffortPath(heights=[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))