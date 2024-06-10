""" 
    Problem statement:
        A school is trying to take an annual photo of all the students. 
        The students are asked to stand in a single file line in non-decreasing order by height. 
        Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
        You are given an iSSndices where heights[i] != expected[i].

        Example 1:
            Input: heights = [1,1,4,2,1,3]
            Output: 3
            Explanation: 
                heights:  [1,1,4,2,1,3]
                expected: [1,1,1,2,3,4]
                Indices 2, 4, and 5 do not match.

        Example 2:
            Input: heights = [5,1,2,3,4]
            Output: 5
            Explanation:
                heights:  [5,1,2,3,4]
                expected: [1,2,3,4,5]
                All indices do not match.

        Example 3:
            Input: heights = [1,2,3,4,5]
            Output: 0
            Explanation:
                heights:  [1,2,3,4,5]
                expected: [1,2,3,4,5]
                All indices match.

        Constraints:
            * 1 <= heights.length <= 100
            * 1 <= heights[i] <= 100
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_sorted = sorted(heights, key=lambda x: x, reverse=False)
        cnt = 0
        for a, b in zip(heights, height_sorted):
            if a != b:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker(heights = [1,1,4,2,1,3]))
    print(s.heightChecker(heights = [5,1,2,3,4]))
    print(s.heightChecker(heights = [1,2,3,4,5]))