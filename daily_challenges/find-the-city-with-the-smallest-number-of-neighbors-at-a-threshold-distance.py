""" 
    URL: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=daily-question&envId=2024-07-26
    1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
    There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
    Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
    Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

    Example 1:
        Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
        Output: 3
        Explanation: The figure above describes the graph.
            The neighboring cities at a distanceThreshold = 4 for each city are:
            City 0 -> [City 1, City 2]
            City 1 -> [City 0, City 2, City 3]
            City 2 -> [City 0, City 1, City 3]
            City 3 -> [City 1, City 2]
            Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

    Example 2:
        Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
        Output: 0
        Explanation: The figure above describes the graph.
            The neighboring cities at a distanceThreshold = 2 for each city are:
            City 0 -> [City 1]
            City 1 -> [City 0, City 4]
            City 2 -> [City 3, City 4]
            City 3 -> [City 2, City 4]
            City 4 -> [City 1, City 2, City 3]
            The city 0 has 1 neighboring city at a distanceThreshold = 2.

    Constraints:
	    * 2 <= n <= 100
	    * 1 <= edges.length <= n * (n - 1) / 2
	    * edges[i].length == 3
	    * 0 <= fromi < toi < n
	    * 1 <= weight[i], distanceThreshold <= 10^4
	    * All pairs (fromi, toi) are distinct.
"""
from typing import List
import math


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Floyd-Warshal algo
        """ 
            let dist be a |V| x |V| array of minimum distances initialized to ∞ (infinity)
            for each edge (u, v) do
                dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
            for each vertex v do
                dist[v][v] ← 0
            for k from 1 to |V|
                for i from 1 to |V|
                    for j from 1 to |V|
                        if dist[i][j] > dist[i][k] + dist[k][j] 
                            dist[i][j] ← dist[i][k] + dist[k][j]
                        end if
        """
        # Initialize the adjacent map
        dist = [[float('inf') for i in range(n)] for j in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        print(dist)

        # Final loop to get the result
        count_dict = {k: 0 for k in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j:
                    if dist[i][j] <= distanceThreshold:     # At most distanceThreshold
                        count_dict[i] += 1
                    if math.isinf(dist[i][j]) and dist[j][i] <= distanceThreshold:
                        count_dict[i] += 1
        print(count_dict)
        count_dict = list(sorted(count_dict.items(), key=lambda x: (x[1], -x[0])))
        print(count_dict)
        return count_dict[0][0]


if __name__ == '__main__':
    s = Solution()
    """ 
    [0, 3, 4, 5]
    [_, 0, 1, 2]
    [_, _, 0, 1]
    [_, _, _, 0]
    """
    print(s.findTheCity(n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=4))
    print(s.findTheCity(n=5, edges=[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold=2))
    """ 
    [[0, _, 8, 15, 18, 9],
     [_, 0, 1, 8,  11, 9],
     [_, _, 0, 7,  10, 8],
     [_, _, _, 0,  3,  8],
     [_, _, _, _,  0,  5],
     [_, _, _, _,  _,  0]]
    """
    print(s.findTheCity(n=6, edges=[[2,3,7],[2,5,8],[0,2,8],[4,5,5],[1,5,10],[3,4,3],[0,5,9],[1,2,1]], distanceThreshold=3269))

    """ 
    [0, 2, 5, 6, 4], 
    [_, 0, 3, 4, 2], 
    [_, _, 0, 1, 2], 
    [_, _, _, 0, 1], 
    [_, _, _, _, 0]
    """
    print(s.findTheCity(n=5, edges=[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold=2))  # Expect 0