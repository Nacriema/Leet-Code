""" 
    Problem statement:
        You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith 
        monster from the city.
        The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.
        You have a weapon that, once fully charged, can eliminate a single monster. Howerver, the weapon takes one minute to charge. The weapon is fully charged at the every start.
        You loose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts at a loss, and the game ends before you can use your weapon.
        Return the maximum number of monsters that you can eliminate before you loose, or n if you can eliminate all the monsters before they reach the city.
        
        Example 1:
            Input: dist = [1,3,4], speed = [1,1,1]
            Output: 3
            Explanation:
            In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
            After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
            After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
            All 3 monsters can be eliminated.
            
        Example 2:
            Input: dist = [1,1,2,3], speed = [1,1,1,1]
            Output: 1
            Explanation:
            In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
            After a minute, the distances of the monsters are [X,0,1,2], so you lose.
            You can only eliminate 1 monster.
        
        Example 3:
            Input: dist = [3,2,4], speed = [5,3,2]
            Output: 1
            Explanation:
            In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
            After a minute, the distances of the monsters are [X,0,2], so you lose.
            You can only eliminate 1 monster.
            
        Constraints:
            * n == dist.length == speed.length 
            * 1 <= n <= 10^5
            * 1 <= dist[i], speed[i] <= 10^5
            
        Hints:
            * Find the ammount of time it takes each monster to arrive
            * 
"""
from typing import List
import math


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # 1. Find the ammount of time it takes each monster to arrive the city 
        times_to_arrive = [math.ceil(a/b) for (a, b) in zip(dist, speed)] 
        print(times_to_arrive)
        
        # 2. Sort the times to arrive
        times_to_arrive.sort()
        
        # 3. Stimulate the playing process 
        time = 0
        for item in times_to_arrive:
            if time < item:
                time += 1
                continue
            else:
                break
        return time
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.eliminateMaximum(dist = [1, 3, 4], speed = [1, 1, 1]))
    print(s.eliminateMaximum(dist = [1, 1, 2, 3], speed = [1, 1, 1, 1]))
    print(s.eliminateMaximum(dist = [3, 2, 4], speed = [5, 3, 2]))
