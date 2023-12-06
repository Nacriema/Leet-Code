""" 
    Problem statement:
    
        Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
        He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. 
        On every subsequent Monday, he will put in $1 more than the previous Monday.
        Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

        Example 1:
            Input: n = 4
            Output: 10
            Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

        Example 2:
            Input: n = 10
            Output: 37
            Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

        Example 3:
            Input: n = 20
            Output: 96
            Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


        Constraints:
            * 1 <= n <= 1000
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks, remain_days = divmod(n, 7)
        print(f'Number of weeks: {num_weeks}, Remain days: {remain_days}')
        
        # Calculate the start ammount for the last week
        start_ammount = 1 + num_weeks
        sum_last_week = remain_days * start_ammount + remain_days * (remain_days - 1) // 2
        
        # Calculate the sum of the num_weeks
        sum_weeks = num_weeks * 28 + (num_weeks - 1) * num_weeks * 7 // 2
        return sum_last_week + sum_weeks


if __name__ == '__main__':
    s = Solution()
    print(s.totalMoney(n=4))
    print(s.totalMoney(n = 10))
    print(s.totalMoney(n = 20))