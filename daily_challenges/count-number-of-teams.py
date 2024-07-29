""" 
    Problem Statement:
        URL: https://leetcode.com/problems/count-number-of-teams/description/?envType=daily-question&envId=2024-07-29
        1395. Count Number of Teams
        There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
        You have to form a team of 3 soldiers amongst them under the following rules:
        Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
        A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
        Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

        Example 1:
            Input: rating = [2,5,3,4,1]
            Output: 3
            Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

        Example 2:
            Input: rating = [2,1,3]
            Output: 0
            Explanation: We can't form any team given the conditions.

        Example 3:
            Input: rating = [1,2,3,4]
            Output: 4

        Constraints:
            * n == rating.length
            * 3 <= n <= 1000
            * 1 <= rating[i] <= 10^5
            * All the integers in rating are unique.
"""
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        rs = 0
        for i in range(1, len(rating) - 1):
            middle = rating[i]
            # Left small, right big
            # Left big, right small
            left_small, right_big, left_big, right_small = 0, 0, 0, 0
            for num in rating[:i]:
                if num > middle:
                    left_big += 1
                elif num < middle:
                    left_small += 1
            for num in rating[i+1:]:
                if num > middle:
                    right_big += 1
                elif num < middle:
                    right_small += 1
            rs += left_small * right_big + left_big * right_small
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.numTeams(rating = [2,5,3,4,1]))
    print(s.numTeams(rating = [2,1,3]))
    print(s.numTeams(rating = [1,2,3,4]))