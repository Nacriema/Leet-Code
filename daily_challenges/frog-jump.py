"""
    Problem Statement:
        - A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. 
          The frog can jump on a stone, but it MUST NOT jump into the water.

        - Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. I
        nitially, the frog is on the first stone and assumes the first jump must be 1 unit.

        - If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
"""
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
            Implement the solution, use DP

            This is the same problem set as I read from FreeCode Camp when finding the solution for solving Dynamic Programming problem 

            Notice, frog just can run forward

            So, at each state S(position, k_unit), the frog can jump into:  
                - S(position + k_unit - 1, k_unit - 1)  # Slowdown speed
                - S(position + k_unit, k_unit)   # Maintain speed
                - S(position + k_unit + 1, k_unit + 1)  # Accelerate
            
            Finding the recurrent relation: 
            
            The frog can reach the current state S(P, K) if it can reach from the previous, mean: 
            
            canCross(p, k) = canCross(p+k-1, k-1) or canCross(p+k, k) or canCross(p+k+1, k+1)

            Determine the edge case
            
        """
        # Add memorization for check (p, k) value
        global memo
        memo = {} 

        def check(p, k, stones):
            """
                Our recursive check function here
            """
            if (p, k) in memo:
                return memo[(p, k)]
            
            # Edge case
            if p not in stones: return False
            elif p > stones[-1]: return False
            elif p == stones[-1]: return True
            elif k <= 0: return False
            
            ans = False
            for step in [-1, 0, 1]:
                # Before exautive search, then 
                # print(f'Incoming check: P: {p+k+step}, K: {k+step}')
                ans = ans or check(p+k+step, k+step, stones)
            # print('=============')
            memo[(p, k)] = ans
            
            return ans

        # Initialy the frog on the first stone
        # Notice: First jump MUST BE 1 Unit
        if stones[1] != 1: return False
        return check(p=stones[1], k=1, stones=stones[1:])

if __name__ == '__main__':
    s = Solution()
    print(s.canCross(stones=[0,1,3,5,6,8,12,17]))  # Expect: True
    print(s.canCross(stones=[0,1,2,3,4,8,9,11])) # Expect: False
    print(s.canCross(stones=[0,2]))  # Expected: False
    