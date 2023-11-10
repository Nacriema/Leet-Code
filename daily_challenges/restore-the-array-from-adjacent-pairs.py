"""
    There is an integer array nums that consists of n unique elements, but you have forgotten it.
    Howerver, you do remember every pair of adjacent elements in nums.
    You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = 
    [u_i, v_i] indicates that the element u_i and v_i are adjacent in nums.
    
    It is guaranteed that every adjacent pair of elements nums[i] and nums[i + 1] will exist in 
    adjacentPairs, either as [nums[i], nums[i + 1]] or [nums[i + 1], nums[i]]. The pairs can 
    appear in any order.
    
    Return the original array nums. If there are multiple solutions, return any of them.
    
    Example 1:
        Input: adjacentPairs = [[2,1],[3,4],[3,2]]
        Output: [1,2,3,4]
        Explanation: This array has all its adjacent pairs in adjacentPairs.
        Notice that adjacentPairs[i] may not be in left-to-right order.
        
    Example 2:
        Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
        Output: [-2,4,1,-3]
        Explanation: There can be negative numbers.
        Another solution is [-3,1,4,-2], which would also be accepted.
        
    Example 3:
        Input: adjacentPairs = [[100000,-100000]]
        Output: [100000,-100000]
        
    Constraints:
        * nums.length == n
        * adjacentPairs.length == n - 1
        * adjacentPairs[i].length == 2
        * 2 <= n <= 10^5
        * -10^5 <= nums[i], ui, vi <= 10^5
        * There exists some nums that has adjacentPairs as its pairs.
"""
from typing import List
from collections import deque


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 1. Find the start point of the chain (there are exactly 2 - 2 numbers that appear just one time) 
        table = dict() # type: dict
        edges = dict()

        for pair in adjacentPairs:
            tmp = edges.get(pair[0], [])
            edges[pair[0]] = tmp + [pair[1]]

            tmp = edges.get(pair[1], [])
            edges[pair[1]] = tmp + [pair[0]]
            
            for num in pair:
                if table.get(num, 0) != 0:
                    del table[num]
                else:
                    table.update({num: 1})

        start_point = list(table.keys())[0]

        # Perform depth first search
        paths = deque()
        paths.append(({start_point: 1}, start_point))

        while len(paths):
            current, latest_node = paths.popleft()
            if len(current) == len(adjacentPairs) + 1:
                return list(current.keys())
            
            for next_node in edges[latest_node]:
                if next_node not in current.keys():
                    current.update({next_node: 1})
                    paths.append((current, next_node))


if __name__ == '__main__':
    s = Solution()
    print(s.restoreArray(adjacentPairs = [[2, 1], [3, 4], [3, 2]]))
    print(s.restoreArray(adjacentPairs = [[4, -2], [1, 4], [-3, 1]]))
    print(s.restoreArray(adjacentPairs = [[100000, -100000]]))