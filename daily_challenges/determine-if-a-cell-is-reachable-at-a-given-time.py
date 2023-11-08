""" 
    Problem statement:
        You are given four integers sx, sy, fx, fy, and a non-negative integer t.
        
        In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.
        
        Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.
        
        A cell's adjacent cells are the 8 cells arround it that share at least one corner with it. You can visit the same cell 
        several times.
        
        Example 1:
            Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
            Output: true
            Explanation: 
                Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted 
                in the picture above.
        
        Example 2:
            Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
            Output: false
            Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells
            depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.
            
        Constraints:
            * 1 <= sx, xy, fx, fy <= 10^9
            * 0 <= t <= 10^9
            
        Brain storming:
            * In this problem, I need to find the fastest time I can take to reach from the start point to the end point.
            * There are 3 cases that I need to consider (A vertical rectange, a horizontal rectange and a square) 
                * Horizontal rectangle:
                * Vertical rectangle:
                * Square: 
"""
import math


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Find the shortest time to reach from start to finish point
        # 1. Horizontal rectangle
        delta_x = int(math.fabs(fx - sx))
        delta_y = int(math.fabs(fy - sy))
        min_time = 0
        
        if delta_x > delta_y:
            min_time = (delta_x - delta_y) + delta_y
        elif delta_y > delta_x:
            min_time = (delta_y - delta_x) + delta_x
        else:
            min_time = delta_y
        
        print(f'Min time: {min_time}')
        
        # Handle the edge case: 
        if min_time == 0:
            if t == 1:
                return False
            return True
        
        return min_time <= t    
    
if __name__ == '__main__':
    s = Solution()
    print(s.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6))
    print(s.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3))
    print(s.isReachableAtTime(sx = 1, sy = 1, fx = 1, fy = 2, t = 0))
    print(s.isReachableAtTime(sx = 1, sy = 1, fx = 1, fy = 3, t = 2))  
    print(s.isReachableAtTime(sx = 1, sy = 1, fx = 4, fy = 3, t = 2))
    print(s.isReachableAtTime(sx = 1, sy = 2, fx = 1, fy = 2, t = 1))  # Expect: False
    print(s.isReachableAtTime(sx = 1, sy = 1, fx = 1, fy = 1, t = 3))  # Expect: True