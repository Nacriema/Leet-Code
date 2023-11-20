""" 
    Problem statement:
        You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
        You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.
        There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.
        Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

        Return the minimum number of minutes needed to pick up all the garbage.
        
        Example 1:
            Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
            Output: 21
            Explanation:
                The paper garbage truck:
                    1. Travels from house 0 to house 1
                    2. Collects the paper garbage at house 1
                    3. Travels from house 1 to house 2
                    4. Collects the paper garbage at house 2
                Altogether, it takes 8 minutes to pick up all the paper garbage.
                The glass garbage truck:
                    1. Collects the glass garbage at house 0
                    2. Travels from house 0 to house 1
                    3. Travels from house 1 to house 2
                    4. Collects the glass garbage at house 2
                    5. Travels from house 2 to house 3
                    6. Collects the glass garbage at house 3
                Altogether, it takes 13 minutes to pick up all the glass garbage.
                Since there is no metal garbage, we do not need to consider the metal garbage truck.
                Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
        
        Example 2:
            Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
            Output: 37
            Explanation:
                The metal garbage truck takes 7 minutes to pick up all the metal garbage.
                The paper garbage truck takes 15 minutes to pick up all the paper garbage.
                The glass garbage truck takes 15 minutes to pick up all the glass garbage.
                It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.

        Constraints:
            * 2 <= garbage.length <= 10^5
            * garbage[i] consists of only the letters 'M', 'P', and 'G'.
            * 1 <= garbage[i].length <= 10
            * travel.length == garbage.length - 1
            * 1 <= travel[i] <= 100
            
        Hints: 
            * Where can we save time ? By not visist all the houses
            * For each type of garbage, find the house with the highest index that has at least 1 unit type of garbage
"""
from typing import List
from collections import defaultdict, Counter

class Solution:
    def garbageCollection_SLOW(self, garbage: List[str], travel: List[int]) -> int:
        last_dict = defaultdict(lambda: -1)
        for i, g in enumerate(garbage[::-1]):
            for item in ["G", "P", "M"]:
                if last_dict[item] == -1 and item in g:
                    last_dict[item] = len(garbage) - 1 - i
        # Again, looping time for each truck anc calculate the time
        total_time = 0
        
        for item in ["G", "P", "M"]:
            last = last_dict[item]
            if last == -1:
                continue
            else:
                for i in range(0, last + 1):
                    if i > 0: total_time += travel[i - 1]
                    freq = Counter(garbage[i]) 
                    if item in freq.keys():
                        total_time += freq[item]
        return total_time

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0

        n = len(garbage)

        m,p,g = False,False,False
        for i in range(n-1,-1,-1):
            if not g and "G" in garbage[i]:
                g=True
                ans+=sum(travel[:i])
            if not m and "M" in garbage[i]:
                m=True
                ans+=sum(travel[:i])
            if not p and "P" in garbage[i]:
                p=True
                ans+=sum(travel[:i])
            if all([m,p,g]):
                break

        return len("".join(garbage))+ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.garbageCollection(garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3]))
    print(s.garbageCollection(garbage = ["MMM", "PGM", "GP"], travel = [3, 10]))