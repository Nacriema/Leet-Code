"""
    Problem Statement:
        URL: https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
        624. Maximum Distance in Arrays
        You are given m arrays, where each array is sorted in ascending order.
        You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
        Return the maximum distance.

        Example 1:
            Input: arrays = [[1,2,3],[4,5],[1,2,3]]
            Output: 4
            Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

        Example 2:
            Input: arrays = [[1],[1]]
            Output: 0

        Constraints:
            * m == arrays.length
            * 2 <= m <= 10^5
            * 1 <= arrays[i].length <= 500
            * -10^4 <= arrays[i][j] <= 10^4
            * arrays[i] is sorted in ascending order.
            * There will be at most 105 integers in all the arrays.
"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key=lambda x: (x[0]))
        max_so_far = -float('inf')
        minimum = arrays[0][0]
        maximum = arrays[0][-1]
        for array in arrays[1:]:
            max_so_far = max(max_so_far, abs(array[-1] - minimum), abs(maximum - array[0]))
        return max_so_far


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]]))
    print(s.maxDistance(arrays = [[1],[1]]))