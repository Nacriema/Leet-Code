"""
    Problem statement:
        You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position
        to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time)

        Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly
        steps steps. Since the answer may be too large, return it modulo 10^9 + 7

        Example 1: 
            Input: steps = 3, arrLen = 2
            Output: 4
            Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
            Right, Left, Stay
            Stay, Right, Left
            Right, Stay, Left
            Stay, Stay, Stay

        Example 2:
            Input: steps = 2, arrLen = 4
            Output: 2
            Explanation: There are 2 differents ways to stay at index 0 after 2 steps
            Right, Left
            Stay, Stay

        Example 3:
            Input: steps = 4, arrLen = 2
            Output: 8

        Constraints: 
            * 1 <= steps <= 500
            * 1 <= arrLen <= 10^6

        Brain storming:
            * May be I can find the math fomular for this problem ???
            * If I found a solution, then the A() will be use in this case
            * Number of Right == Number of Left: in order to make the move still 0, and of course can have Number of Right == Number of Left == 0
            * Notice: The pointer should not be placed outside the array at any time - mean that the A() at point 2 must be divided by 2
            * No, in this problem, we have the another argument called arrLen :<
        
            => We can not solve this by math, try difference approach like DP
            DP(pos, steps): Number of ways to back to origin 0 from the CURRENT position pos and the remaining steps
            (pos >= 0 and steps >= 0)
            
        Hints:
            * Try with Dynamic Programming DP(pos, steps): Number of ways to back to the position 0 using exactly "steps" move
            * Notice that tha computational complexity does not depend of "arrLen"
"""
from math import inf


class Solution:
    def numWays_SLOW(self, steps: int, arrLen: int) -> int:
        @cache
        def DP(pos, step):
            print(f'Pos: {pos}, Remain step: {step}')
            if step == 0:
                if pos == 0:
                    return 1
                return 0
            
            ans = DP(pos, step-1) % MOD # Number of stays state
            if pos > 0:
                ans = (ans + DP(pos-1, step-1)) % MOD  # Number of move left
            if pos < arrLen - 1:
                ans = (ans + DP(pos+1, step-1)) % MOD
            return ans
        MOD = 10**9+7
        return DP(pos=0,step=steps)
    
    def numWays(self, steps: int, arrLen: int) -> int:
        """
            Not use the recursion, instead use additional memory
        """
        m = steps
        n = min(steps // 2 + 1, arrLen)

        dp = [[0] * n for _ in range(m + 1)]

        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, m + 1):
            for j in range(n):
                dp[i][j] = dp[i-1][j]  
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if j < n - 1:
                    dp[i][j] += dp[i-1][j+1]

        return dp[m][0] % mod


if __name__ == '__main__':
    s = Solution()
    # print(s.numWays(steps=3, arrLen=2))
    print(s.numWays(steps=2, arrLen=4))
    # print(s.numWays(steps=4, arrLen=2))