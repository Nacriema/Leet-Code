"""
    Problem statement:
        You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the 
        time taken to paint n different walls respectively. There are two painters available:
            * A paid painter that paints the ith wall in time[i] units of time an take cost[i] units of money.
            * A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can 
            only be used if the paid painter is already occupied.

        Return the mimimum amount of money required to paint the n walls.

        Example 1:
            Input: cost = [1,2,3,2], time = [1,2,3,2]
            Output: 3
            Explanation: The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time;
            meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. 
            Thus, the total cost is 1 + 2 = 3.

        Example 2: 
            Input: cost = [2,3,4,2], time = [1,1,1,1]
            Output: 4
            Explanation: The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; 
            meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. 
            Thus, the total cost is 2 + 2 = 4.

        Constraints:
            * 1 <= cost.length <= 500
            * cost.length == time.length
            * 1 <= cost[i] <= 10^6
            * 1 <= time[i] <= 500

        Hint:
            * Can we break the problem down into smaller subproblems and use DP ?
            * Paid painters will be used for a maximum of N/2 uints of time. There is no need to use paid painter for a time 
            greater than this.
        
        Brain strorming:
            * Paid painter hired time >= Free painter using time
            * Try to exploit the paid painter to paint >=50% of the time and take the least cost wall as much as possible

"""
from typing import List
from math import inf

class Solution:
    def paintWalls_Greedy(self, cost: List[int], time: List[int]) -> int:
        """
            Use Greedy failed
                Test case: cost=[26,53,10,24,25,20,63,51], time=[1,1,1,1,2,2,2,1]
                Sorted cost time [(10, 1), (20, 2), (24, 1), (25, 2), (26, 1), (51, 1), (53, 1), (63, 2)]
                Expected 55 -> My algorithm returned 79
        """
        total_time = len(time)
        print(f'Total time: {total_time}')
        # 1. Zip them into pair
        cost_time = list(zip(cost, time))
        print(f'Cost time: {cost_time}')

        # 2. Sort the cost_time base on the cost first, if cost are equal, then choose the larger time among them
        cost_time = sorted(cost_time, key=lambda x: (x[0], -x[1]))
        print(f'Sorted cost time {cost_time}')

        # 3. Looping from this array, accumulate the cost and
        min_cost = 0
        used_time = 0
        idx = 0

        while not (used_time >= (len(time) - idx)):
            print(f'Used time: {used_time}')
            min_cost += cost_time[idx][0]
            used_time += cost_time[idx][1]
            idx += 1
        print(f"Used time: {used_time}, Id: {idx}")
        return min_cost
    
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        """
            If we have the paid painter paint the ith wall. It cost us cost[i] money.
            The paid painter will paint 1 wall and occupied for time[i] time.
            While the paid painter is occupied, the free painter can paint time[i] walls.
            => We spent cost[i] money to paint 1 + time[i] wall

            DP[i, remain] is the function that returns the minimum cost to paint remain walls when consider all index >= i
                Base: 
                    remain <= 0 -> DP[i, remain] = 0
                    i == n -> DP[i, remain], we run out of walls to put the paid painter. Return infinity
                For the ith wall, we have 2 option. We can hire the paid painter to this wall or not hire them
                    - If hire them, we spend cost[i] and paint 1 + time[i] wall. Thus the cost of this option is:  
                        cost[i] + DP[i+1, remain - 1 - time[i]]
                    - If we dont hire them, simply move to the next index. Cost for this option is:
                        DP[i + 1, remain]
                Then: 
                    DP[i, remain] = min(DP[i + 1, remain], cost[i] + DP[i+1, remain - 1 - time[i]])    
        """
        memo = dict()
        def DP(i, remain):
            tmp = memo.get((i, remain), -1)
            if tmp != -1:
                return tmp
            if remain <= 0:
                return 0
            if i == n:
                return inf
            dont_paint = DP(i + 1, remain)
            paint = cost[i] + DP(i+1, remain - 1 - time[i])
            return min(paint, dont_paint)

        n = len(cost)
        return DP(0, n)


if __name__ == '__main__':
    s = Solution()
    # print(s.paintWalls(cost=[1,2,3,2], time=[1,2,3,2]))
    # print(s.paintWalls(cost=[2,3,4,2], time=[1,1,1,1]))
    # print(s.paintWalls(cost=[8,7,5,15], time=[1,1,2,1]))
    # print(s.paintWalls(cost=[42,8,28,35,21,13,21,35], time=[2,1,1,1,2,1,1,2]))  # Want 63
    # print(s.paintWalls(cost=[49,35,32,20,30,12,42], time=[1,1,2,2,1,1,2]))
    print(s.paintWalls(cost=[26,53,10,24,25,20,63,51], time=[1,1,1,1,2,2,2,1])) # Want 55
