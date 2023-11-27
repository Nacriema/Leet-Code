""" 
    Problem statement:
        The chess knight has a unique movement, it may move two squares vertically and one square horizontally, 
        or two squares horizontally and one square vertically (with both forming the shape of an L). 
        The possible movements of chess knight are shown in this diagaram:

        A chess knight can move as indicated in the chess diagram below:
        We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

        Given an integer n, return how many distinct phone numbers of length n we can dial.
        You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial
        a number of length n. All jumps should be valid knight jumps.

        As the answer may be very large, return the answer modulo 10^9 + 7.
        
        Example 1:
            Input: n = 1
            Output: 10
            Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

        Example 2:
            Input: n = 2
            Output: 20
            Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

        Example 3:
            Input: n = 3131
            Output: 136006598
            Explanation: Please take care of the mod.

        Constraints:
            * 1 <= n <= 5000
"""
MOD = 10**9+7
DP = [0, 10]
state = [1] * 10
nxt_state = [0] * 10


class Solution:
    def knightDialer_NOT_OPTIMIZED(self, n: int) -> int:
        """ 
            This is the same with the countVowelPermutation problem
        """
        # 1. Create the table (i, j) mean the i+1 length and j-th vowel
        dp = [[0 for i in range(10)] for j in range(n)]
        
        # Base case, all item in first row are 1
        for i in range(10):
            dp[0][i] = 1
        
        if n == 1:
            return sum(dp[n-1])
        
        # Construct the table based on the rule "Ended number can follow by some number"
        table = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # 2. Start counting
        # Check for each line, specify the ending by the index, and then take action for the next line
        for i in range(n - 1):
            for j in range(10):
                if j != 5:
                    for k in table[j]:
                        dp[i + 1][k] += dp[i][j]
                        dp[i + 1][k] %= MOD
        
        return sum(dp[n - 1]) % MOD
    
    
    def knightDialer(self, n: int) -> int:
        graph = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [0,3,9],
            [],
            [0,1,7],
            [2,6],
            [1,3],
            [2,4],
        ]
        global state, nxt_state
        for _ in range(len(DP), n+1):
            nxt_state[:] = [0] * 10
            for cur, ct in enumerate(state):
                for nxt in graph[cur]:
                    nxt_state[nxt] += ct
            for i in range(10):
                nxt_state[i] %= MOD

            DP.append( sum(nxt_state) % MOD )
            state, nxt_state = nxt_state, state
        
        return DP[n]
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.knightDialer(n=1))
    print(s.knightDialer(n=2))
    print(s.knightDialer(n=3131))