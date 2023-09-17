"""
    Problem Statement:
        You have an UNDIRECTED, connected graph of n nodes labeled from 0 to n-1. You are given an array 
        graph where graph[i] is a list of all the nodes connected with node i by an edge.

        Return the length of the shortest path that visits every node. You may start and stop at any node,
        you may revisit nodes multiple times and you may reuse edges

    Example 1: 
        Input: graph = [[1,2,3],[0],[0],[0]]
        Output: 4
        Explanation: One possible path is [1,0,2,0,3]

    Example 2:
        Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
        Output: 4
        Explanation: One possible path is [0,1,4,2,3]

        
    Constrains:
        * n == graph.length
        * 1 <= n <= 12
        * 0 <= graph[i].length < n
        * graph[i] does not contain i
        * If graph[a] contains b, then graph[b] contains [a]
        * The input graph is always connected

    Idea:
        Use BFS with mask       
"""
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        """
        n = len(graph)
        
        # Final mask when all the node will be visited
        finalMask = (1<<n) - 1
        
        # Initialize a queue for BFS which will store current
        # node id and mask of visited nodes.
        q = []
        
        # Initialize a visited array for keeping track
        # of all mask that are visited in the path, each will keep track for the starting node -> 
        visited = [[0 for i in range(finalMask+1)] for j in range(n)]

        print(f'Visited array: {visited}')
        
        # Push starting node for
        # all possible path with their mask
        for i in range(n):
            q.append([i,1<<i])

        print(f"Queue: {q}")
        
        # For counting the minimum time
        # to visit all the nodes
        timeCount = 0
        
        while len(q):
            size = len(q)
            
            # Iterate over each level
            for i in range(size):
                
                # Fetch and pop the current node
                curr = q.pop(0)
                
                # Check if the current node mask
                # is equal to finalMask
                if(curr[1] == finalMask):
                    print(f"Final mask: {finalMask}")
                    return timeCount
                
                # Explore all the child of current node
                for child in graph[curr[0]]:
                    
                    # Make a new Mask for child
                    newVisitedBit = curr[1]|(1<<child)
                    
                    # If new Mask for child has
                    # not been visited yet,
                    # push child and new Mask in
                    # the queue and mark visited
                    # for child with newVisitedBit
                    if(visited[child][newVisitedBit] == False):
                        q.append([child,newVisitedBit])
                        visited[child][newVisitedBit] = True
                        
        
            # Increment the time Count after each level
            timeCount = timeCount + 1
        
        # If all node can't be visited
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathLength(graph=[[1,2,3],[0],[0],[0]]))
    print(s.shortestPathLength(graph=[[1],[0,2,4],[1,3,4],[2],[1,2]]))

