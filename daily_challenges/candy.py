"""
    Problem Statement:
        There are n children standing in a line. Each child is assingned a rating value given in the integer array ratings.
        You are givin candies to these children subjected to the following requirements:
            * Each child must have at least one candy.
            * Children with a higher rating get more candies than their neighbors.
        
        Return the minimum number of candies you need to have to distribute the candies to the children.
        
    Example 1:
        Input: ratings = [1,0,2]
        Output: 5
        Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
        
    Example 2:
        Input: ratings = [1,2,2]
        Output: 4
        Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
        The third child gets 1 candy because it satisfies the above two conditions.
        
    Constrains:
        * n == ratings.length
        * 1 <= n <= 2 * 10 ^ 4
        * 0 <= ratings[i] <= 2 * 10^4
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
            Based on the constrains, may be I need a DP solution or a Single loop with Greedy
            
            - Loop from left to right
            - Consider at index i, the neighbors are i + 1 and i - 1:
                + Compare between i + 1 and i: 
                    * r[i+1] > r[i] -> r[i+1] = r[i] + 1
                    * r[i+1] <= r[i] -> just skip this children
                + Consider to compare between i - 1 and i. Humm, maybe we dont need this comparison. 
                
            - Just one loop is not enough, we need a second loop from the back to check the other cases
        """
        n_children = len(ratings)
        candies = [1] * n_children
        
        for i in range(n_children - 1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
        
        print(f'Candies 1: {candies}')
                
        for i in range(n_children - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
        
        print(f'Candies: {candies}')
        return sum(candies)
        
        
if __name__ == '__main__':
    s = Solution()
    # print(s.candy(ratings=[1, 0, 2]))
    # print(s.candy(ratings=[1, 2, 2]))
    # print(s.candy(ratings=[1, 3, 2, 2, 1]))
    print(s.candy(ratings=[1, 2, 87, 87, 87, 2, 1]))  #  Expect: 13