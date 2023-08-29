"""
    Problem Statement:
        You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
            * If the ith character is 'Y', it means that customers come at the ith hour
            * Whereas 'N' indicates that no customers come at the ith hour.

        If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
            * For every hour when the shop is open and no customers come, the penalty increases by 1.
            * For every hour when the shop is closed and customers come, the penalty increases by 1.

        
        TARGET: Return the earliest hour at which the shop must be closed to incur a minimum penalty.
                Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.


    Test Cases:
        Input: customers = "YYNY" -> Output: 2
        Input: customers = "NNNNN" -> Output: 0
        Input: customers = "YYYY" -> Output: 4
        
    Constrains:
        * 1 <= customers.length <= 10^5 (The maximum hours)
        * Customers consists only of characters 'Y' and 'N'.

"""
from collections import Counter


class Solution:
    def bestClosingTime(self, customer: str) -> int:
        """
            Implementation here
            
            Use 2 loops here, and 2 another variables
            - One variable for total number of Y: nY -> total number of N: nN = len(customer) - nY
            
            Assume we are at index i, call number pre-index N: preN, call number after-index Y: aftY => our penalty at index i is: penalty[i] = preN + aftY
            
            At index i, call one value for preN -> preY = i - preN -> aftY = nY - preY = nY - (i - preN) = nY + preN - i 
            
            So penalty[i] = preN + aftY = preN + nY + preN - i = 2 * preN + nY - i 
        """
        # 1. Use counter to get the number of Y and N in the customer string
        freq = dict(Counter(customer))
        nY = freq.get('Y', 0)
        
        # 2. Loop and given the tracked min penalty index
        min_index = 0
        min_penalty = len(customer) + 2
        preN = 0
        
        # 3. Cheat to loop all hours
        customer += " "
        
        for i, char in enumerate(customer):
            if char == 'N': 
                preN += 1
                penalty = 2 * max(preN - 1, 0) + nY - i
            else:
                penalty = 2 * preN + nY - i
            if penalty < min_penalty:
                min_penalty = penalty
                min_index = i
        
        return min_index
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.bestClosingTime(customer="YYNY"))  # Expect 2
    # print(s.bestClosingTime(customer="NNNNN"))
    # print(s.bestClosingTime(customer="YYYY"))
    # print(s.bestClosingTime(customer="NYYYNNNYNN"))