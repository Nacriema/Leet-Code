"""
    Problem Statement:
        Given n orders, each order consist in pucjup and delivery services.
        Count all valid pickup/delivery possible sequences such that delivery(i) is always after 
        of pickup(i)
        Since the answer may be too large, return it modulo 10^9 + 7


    Example 1:
        Input: n = 1
        Output: 1
        Explanation: Unique order (P1, D1) Delivery 1 always is after of Pickup 1.

    Example 2: 
        Input: n = 2
        Ouput: n = 6
        Explanation: All possible orders:
            (P1, P2, D1, D2), (P1, P2, D2, D1),
            (P1, D1, P2, D2), (P2, P1, D1, D2),
            (P2, P1, D2, D1) and (P2, D2, P1, D1)

            This is an valid order (P1, D2, P2, D1) because Pickup 2 is after of Delivery 2.

    Example 3:
        Input: n = 3
        Ouput: 90
    
    Constrains:
        1 <= n <= 500

    Idea: This problem absolutely the DP problem
    May be this problem has the O(1) solution ? Yes, may be we can have the generic solution !!!
    
    Hint: Use the permutation and combination theory to add one (P, D) pair each time until n pairs
    So: We come up with the DP problem where DP[i+ 1] = ? DP[i]

    This problem is like Combination Sum IV problem
"""


class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0] * (n + 1)  # From 0 order to n orders
        
        # Base case
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            # Use permutation and combination theory to add one (P, D) pair to the existed one
            # dp[i + 1] = dp[i] * (tmp * (tmp + 1)) // 2 with tmp = 2 * i + 1
            tmp = 2 * (i - 1) + 1
            dp[i] = dp[i - 1] * (tmp * (tmp + 1)) // 2
            
        return dp[n] % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.countOrders(n=1))
    print(s.countOrders(n=2))
    print(s.countOrders(n=3))