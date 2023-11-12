"""
    Problem statement:
        There is a directed weighted graph that consists of n nodes numbered from 0 to n-1. The edges of the graph 
        are initially represented by the given array edges where edges[i] = [from_i, to_i, edgeCost_i] meaning that 
        there is and edge from from_i to to_i with the cost edgeCost_i.

        Implement the Graph class:
            * Graph(int n, int[][] edge) initializes the object with n nodes and the given edges.
            * addEdge(int[] edge) add an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed 
            that there is no edge between the two nodes before adding this one.
            * int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path 
            exist, return -1. The cost of a path is the num of the costs of the edges in the path.

        Example 1:
            Input
                ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
                [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
            Output
                [null, 6, -1, null, 6]

            Explanation
                Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
                g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
                g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
                g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
                g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.

        Constraints:
            * 1 <= n <= 100
            * 0 <= edges.length <= n * (n - 1)
            * edges[i].length == edge.length == 3
            * 0 <= fromi, toi, from, to, node1, node2 <= n - 1
            * 1 <= edgeCosti, edgeCost <= 10^6
            * There are no repeated edges and no self-loops in the graph at any point.
            * At most 100 calls will be made for addEdge.
            * At most 100 calls will be made for shortestPath.
"""
from typing import List
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # Source node is always 0
        self.V = n # Number of vertex
        self.adj = [[] for _ in range(n)]

        # Update the adjacent matrix
        for edge in edges:
            self.addEdge(edge=edge)

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        # Create a priority queue to store verticies that are being processed
        pq = []
        heapq.heappush(pq, (0, node1))

        # Create a vector for distances and initialize all distances as infinite
        dist = [float('inf')] * self.V
        dist[node1] = 0

        while pq:
            # First vertex in pair is the minimum distance vertex, extract it from priority queue
            d, u = heapq.heappop(pq)
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u
                if dist[v] > d + weight:
                    # Update distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        if dist[node2] == float('inf'): return -1        
        return dist[node2]

if __name__ == '__main__':
    obj = Graph(n=4, edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(obj.shortestPath(node1=3, node2=2))
    print(obj.shortestPath(node1=0, node2=3))
    print(obj.addEdge(edge=[1, 3, 4]))
    print(obj.shortestPath(node1=0, node2=3))