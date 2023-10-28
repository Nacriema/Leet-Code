"""
    Problem statement:
        Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
            * Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
            * Each vowel 'a' may only be followed by an 'e'
            * Each vowel 'e' may only be followed by an 'a' or an 'i'
            * Each vowel 'i' may not be followed by another 'i'
            * Each vowel 'o' may only be followed by an 'i' or a 'u'
            * Each vowel 'u' may only be followed by an 'a'
        Since the answer may be too large, return it modulo 10^9+7

        Example 1:
            Input: n = 1
            Output: 5
            Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

        Example 2:
            Input: n = 2
            Output: 10
            Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

        Example 3:
            Input: n = 5
            Output: 68

        Constraints:
            * 1 <= n <= 2 * 10^4

        Hints:
            * Use Dynamic Programming 
            * Let DP[i][j] is the number of strings of length i that ends with the j-th vowel
            * Deduce the recurrence from the given relations between vowels.
        
        Brain Storming:
            * Is this have a mat fomular to direcly solve this problem ???
            * Or solving using DP approach 
                - Call DP[i][j] is the number of string has length i and ends with the j-th vowel           
"""
MOD = 10**9 + 7

class Solution:
    def countVowelPermutation_NOT_OPTIMIZED(self, n: int) -> int:
        # 1. Create the table (i, j) mean the i+1 length and j-th vowel
        dp = [[0 for i in range(5)] for j in range(n)]
        
        # Base case, all item in first row are 1
        for i in range(5):
            dp[0][i] = 1
        
        if n == 1:
            return sum(dp[n-1])
        
        # Construct the table based on the rule "ended char can be followed by some char"
        table = {
            0: [1],
            1: [0, 2],
            2: [0, 1, 3, 4],
            3: [2, 4],
            4: [0]
        }

        # 2. Start counting
        # Check for each line, specify the ending by the index, and then take action for the next line
        for i in range(n - 1):
            for j in range(5):
                for k in table[j]:
                    dp[i + 1][k] += dp[i][j]
                    dp[i + 1][k] %= MOD
        
        return sum(dp[n - 1]) % MOD
    
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (o + i) % MOD
        return (a + e + i + o + u) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.countVowelPermutation(n=1))
    print(s.countVowelPermutation(n=2))
    print(s.countVowelPermutation(n=5))
    print(s.countVowelPermutation(n=144))
