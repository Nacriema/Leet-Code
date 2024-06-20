""" 
    Problem statement:
        In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket.
        Rick has n empty baskets, the ith basket is at position[i], 
        Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

        Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
        Given the integer array position and the integer m. Return the required force.

        Example 1: 
            Input: position = [1,2,3,4,7], m = 3
            Output: 3
            Explanation: 
                Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. 
                The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

        Example 2:
            Input: position = [5,4,3,2,1,1000000000], m = 2
            Output: 999999999
            Explanation: We can use baskets 1 and 1000000000.

        Constraints:
            * n == position.length
            * 2 <= n <= 10^5
            * 1 <= position[i] <= 10^9
            * All integers in position are distinct.
            * 2 <= m <= position.length
"""
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """ 
            Hint: 
                * If you can place balls such that the answer is x then you can do it for y where y < x.
                * Similarly if you cannot place balls such that the answer is x then you can do it for y where y > x.
                * Binary search on the answer and greedily see if it is possible.

            Binary search on the gravity domain
        """
        def feasible(grav):
            """
                Greedily check if we can distribute balls to baskets such that meet the grav constrain
            """
            prev_pos = position[0]
            remain_balls = m - 1
            for pos in position[1:]:
                if (pos - prev_pos) >= grav:
                    remain_balls -= 1
                    prev_pos = pos
                if not remain_balls:
                    return True
            return False

        # Sort the basket position
        position.sort()

        # Define search space for Force
        left, right = 1, (position[-1] - position[0]) // (m - 1)
        while left < right:
            mid = left + (right - left) // 2 + 1
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.maxDistance(position = [1,2,3,4,7], m = 3))
    print(s.maxDistance(position = [5,4,3,2,1,1000000000], m = 2))
