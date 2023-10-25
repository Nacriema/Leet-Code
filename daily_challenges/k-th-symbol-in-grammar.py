""" 
    Problem statement:
        We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous
        row and replace each occurence of 0 with 01, and each occurence of 1 with 10.
        
        * For example, for n = 3, the 1st row is 0, the 2nd row is 01 and the 3rd row is 0110.
        Given two integer n and k, return the kth (1-indexed) symbolin the nth row of a table of n rows.
        
        Exampe 1:
            Input: n = 1, k = 1
            Output: 0
            Explanation: row 1: 0
            
        Example 2:
            Input: n = 2, k = 1
            Output: 0
            Explanation: 
            row 1: 0
            row 2: 01
            
        Example 3:
            Input: n = 2, k = 2
            Output: 1
            Explanation: 
            row 1: 0
            row 2: 01
            
        Constraints:
            * 1 <= n <= 30
            * 1 <= k <= 2^(n - 1)
            
        Hints:
            * Try to represent the current (N, K) in terms of some (N-1, prevK). What is prevK ?
"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        """
        lst = []
        while n > 0:
            lst.append((n, k))
            n -= 1
            k = (k + 1) // 2
            
        # Then pop from the lst to check the value
        lst.pop()
        prev = 0  # This is (1, 1)
        
        while len(lst):
            curr = lst.pop()
            if prev == 0:
                if curr[1] % 2 == 0:
                    prev = 1
                else: 
                    prev = 0
            else:
                if curr[1] % 2 == 0:
                    prev = 0
                else:
                    prev = 1
        return prev
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.kthGrammar(n=1, k=1))
    # print(s.kthGrammar(n=2, k=1))
    # print(s.kthGrammar(n=2, k=2))
    print(s.kthGrammar(n=4, k=3))
    