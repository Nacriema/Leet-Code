"""
    Problem Set:
        You are given an array points representing integer coordinates of some points on a 2D plane, where points[i] = [x_i, y_i]
        
        The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance between them |x_i - x_j| + |y_i - y_j|
        
        Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any 
        two points.
        
    Example 1: 
        Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        Output: 20
        
    Example 2:
        Input: points = [[3,12],[-2,5],[-4,1]]
        Output: 18
        
    Constrains:
        * 1 <= points.length <= 1000
        * -10^6 <= x_i, y_i <= 10^6
        * All pair (x_i, y_i) are distinct.
        
    Hints:
        * Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points
        * The problem is now the coset of minimum spanning tree (MST) in graph with above edges
"""
from typing import List
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            Implementation
            1. Connect each pair of points with a weighted edge
            2. Use Kruskal's Algorithm to solve the MST (Minimum Spanning Tree) problem
                - Sort all the edges in non-decreasing order of the weight
                - Pick the smallest edge. Check if it form the cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it.
                - Repeat step 2 util there have V - 1 edges in the spanning tree (V is the number of verticies - points)
        """
        # A class to represent a graph object
        class Graph:
            # Constructor
            def __init__(self, edges, n):
                self.adjList = [[] for _ in range(n)]

                # add edges to the undirected graph (add each edge once only to avoid
                # detecting cycles among the same edges, say x -> y and y -> x)
                for (src, dest) in edges:
                    self.adjList[src].append(dest)
        
        # A class to represent a disjoint set
        class DisjointSet:
            # Parent contains key, val (node: parent_of_node)
            parent = {}
            
            def makeSet(self, n):
                # Init n node, initially, they are not connected, so parent[node] = node
                for i in range(n):
                    self.parent[i] = i
                
            # Find the root of the set in which element `k` belongs
            def find(self, k):
                """
                    Find the root node of the given node
                """
                if self.parent[k] == k:
                    return k
                return self.find(self.parent[k])
            
            # Perform Union of two subsets
            def union(self, a, b):
                # find the root of the sets in which elements `x` and `y` belongs
                x = self.find(a)
                y = self.find(b)
                self.parent[x] = y
        
        
        def manhattan_dis(a, b):
            return math.fabs(a[0] - b[0]) + math.fabs(a[1] - b[1])
        
        edges = []
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((i, j, manhattan_dis(points[i], points[j])))
        
        # Sort the table of edges in non-decreasing order 
        edges = list(sorted(edges, key=lambda x: x[2]))
        
        # Implement the Kruskal's algorithm
        
        # Initialize `DisjointSet` class
        ds = DisjointSet()
        ds.makeSet(len(points))
        added_veticies = 0
        rs = 0
        
        while added_veticies < len(points) - 1:
            # Consider to pick up the edges from
            for edge in edges:
                source, dest, distance = edge
                # Find the root of the sets to which elements `u` and `v` belongs
                root_source = ds.find(source)
                root_dest = ds.find(dest)
                # if both `u` and `v` have the same parent, the cycle is found
                if root_source == root_dest:
                    # Cycle found, so dont use this
                    continue
                else:
                    # Use this
                    ds.union(source, dest)
                    added_veticies += 1
                    rs += distance
        return int(rs)


if __name__ == "__main__":
    s = Solution()
    # print(s.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(s.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]]))