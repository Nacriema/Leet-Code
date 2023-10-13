""" 
    Problem Statement:
        You are given an integer array cost where cost[i] is the cost of i_th step on a staircase. 
        Once you pay the cost, you can either climb one or two steps.
        
        You can either start from the step with index 0, or the step with index 1.
        
        Return the minimum cost to reach the top of the floor.
        
        Example 1:
            Input: cost = [10,15,20]
            Output: 15
            Explanation: You will start at index 1.
            - Pay 15 and climb two steps to reach the top.
            The total cost is 15.
            
        Example 2:
            Input: cost = [1,100,1,1,1,100,1,1,100,1]
            Output: 6
            Explanation: You will start at index 0.
            - Pay 1 and climb two steps to reach index 2.
            - Pay 1 and climb two steps to reach index 4.
            - Pay 1 and climb two steps to reach index 6.
            - Pay 1 and climb one step to reach index 7.
            - Pay 1 and climb two steps to reach index 9.
            - Pay 1 and climb one step to reach the top.
            The total cost is 6.
            
        Constraints:
            * 2 <= cost.length <= 1000
            * 0 <= cost[i] <= 999
            
        This problem myst be solved by DP !!!
        
        Top-Down:
            * DP[i]: minCost to reach the step ith of the floor 
            * Recursion: 
                - 1st: i is the result of step 1 step from [i-1] - DP[i] = DP[i-1] + cost[i-1]
                - 2nd: i is the result of step 2 steps from [i-2] - DP[i] = DP[i-2] + cost[i-2]
            
                And DP[i] = min(DP[i-1] + cost[i-1], DP[i-2] + cost[i-2])
                
                Notice: DP[0] and DP[1] = 0 for 2 cases  -> Just call this recursive once
                
                Consider to add memorization
"""
from typing import List


class Solution:
    def minCostClimbingStairs_SLOW(self, cost: List[int]) -> int:
        memo = dict()
        def DP(i):
            if i in (0, 1):
                return 0
            if i in memo.keys():
                return memo[i]
            ans = min(DP(i - 1) + cost[i-1], DP(i-2) + cost[i-2])
            memo[i] = ans
            return ans
        
        return DP(i=len(cost))
    

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs(cost = [10,15,20]))
    print(s.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))