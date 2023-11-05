"""
    Problem statement:
        Given an integer array arr of distinct integers and an integer k.

        A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each 
        round of the game, we compare arr[0] with arr[1], the larger wins and remains at position 0, and the 
        smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

        Return the integer which win the game.

        It is guaranteed that there will be a winner of the game.

        Example 1:
            Input: arr = [2,1,3,5,4,6,7], k = 2
            Output: 5
            Explanation: 
                Let's see the rounds of the game:
                Round |       arr       | winner | win_count
                1     | [2,1,3,5,4,6,7] | 2      | 1
                2     | [2,3,5,4,6,7,1] | 3      | 1
                3     | [3,5,4,6,7,1,2] | 5      | 1
                4     | [5,4,6,7,1,2,3] | 5      | 2
                So we can see that 4 rounds will be played and 5 is the winner because it wins 
                2 consecutive games.
        
        Example 2:
            Input: arr = [3,2,1], k = 10
            Output: 3
            Explanation: 3 will win the first 10 rounds consecutively.

        Constraints:
            * 2 <= arr.length <= 10^5
            * 1 <= arr[i] <= 10^6
            * arr contains distinct integers
            * 1 <= k <= 10^9

        Hints: 
            * If k >= arr.length return the max element of the array.
            * If k < arr.length simulate the game until a number wins k consercutive game.

        Brain storming:
            * When reaching arr.length comparision, the array has been sorted.
"""
from typing import List


class Solution:
    def getWinner_Slow(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        else:
            table = dict()
            # Simulate the game unil we see the winner
            while True:
                if arr[0] > arr[1]:
                    cnt = table.get(arr[0], 0)
                    if cnt + 1 == k:
                        return arr[0]
                    else:
                        table[arr[0]] = cnt + 1
                    
                    arr.append(arr.pop(1)) 
                else:
                    cnt = table.get(arr[1], 0)
                    if cnt + 1 == k:
                        return arr[1]
                    else:
                        table[arr[1]] = cnt + 1
                    arr.append(arr.pop(0))
                print(arr)
    
    def getWinner(self, arr: List[int], k: int) -> int:
        """
            Greedy Algorithm
        """
        count = 0
        winner = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                count = 1
            else:
                count += 1

            if count == k:
                return winner
            
        return winner


if __name__ == '__main__':
    s = Solution()
    print(s.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k = 2))
    print(s.getWinner(arr=[1, 25, 35, 42, 68, 70], k = 3))
    print(s.getWinner(arr=[3, 2, 1], k = 10))