"""
    Problem statement:
        Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y plane.
        Return the maximum number of points that line on the same straight line.
        
    Example 1:
        Input: points = [[1,1],[2,2],[3,3]]
        Output: 3
    
    Example 2:
        Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        Output: 4
        
    Constrains:
        * 1 <= points.length <= 300
        * points[i].length = 2
        * -10^4 <= x_i <= y_i <= 10^4
        * All the points are unique
"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
            My implementation here
            
            Idea: One loop
                1. Loop through the points, calculate the slope of the line formed by [0, 0] and [x_i, y_i] and then add it into the dictionary with key is the slope, and value is frequency angle
                2. Heapify the dictionary
            
            NOTE: 
                - Heapq use the first features to perform sort
                - The smaller the key, then the higher the priority. So in my case I want the max frequency -> negative 
        """
        def slope(point, pivot):
            """
                Given a 2D point, calculate the slope between this point and (0, 0), notice the edge case
            """
            if (point[0] - pivot[0]) == 0:
                return 999
            m = (point[1] - pivot[1]) / (point[0] - pivot[0])
            return m
        
        # Construct the frequencies map
        def max_list_points(list_point):
            freq_dict = {}
            pivot_point = list_point[0]
            
            for point in list_point[1:]:
                sl = slope(point, pivot_point)
                freq_dict[sl] = freq_dict.get(sl, 0) + 1
                
            # Loop again to the freq dict and track the largest frequency
            print(f"Frequency map: {freq_dict}")
            ans = 0
            for _, v in freq_dict.items():
                ans = max(ans, v)
            
            return ans + 1
        
        rs = 0
        for pivot in range(len(points)):   # 
            list_point = points[pivot:] + points[:pivot]
            print(f'List point: {list_point}')
            print(f'Max list point inside this list_points: {max_list_points(list_point)}')
            rs = max(rs, max_list_points(list_point))
        
        print(f'Final: {rs}')
        return rs


if __name__ == '__main__':
    s = Solution()
    points_1 = [[1,1],[2,2],[3,3]]
    points_2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # print(s.maxPoints(points=points_2))
    # print(s.maxPoints(points=points_1))
    
    # Failed test case
    points_3 = [[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]]
    print(f'Length of points: {len(points_3)}')
    
    # Expected 6, but output give 10 ?
    print(s.maxPoints(points=points_3))

    points_4 = [[0, 0]]
    print(s.maxPoints(points=points_4))
    