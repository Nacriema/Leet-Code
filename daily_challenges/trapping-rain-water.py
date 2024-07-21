""" 
    Problem Statement:
        URL: https://leetcode.com/problems/trapping-rain-water/description/
        42. Trapping Rain Water
        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        Example 1:
            Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
            Output: 6
            Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

        Example 2:
            Input: height = [4,2,0,3,2,5]
            Output: 9

        Constraints:
            * n == height.length
            * 1 <= n <= 2 * 10^4
            * 0 <= height[i] <= 10^5
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """ 
            water[i] = min(max_left_height, max_right_height) - arr[i]
        """
        # Construct the 2 max array
        max_1 = [None] * len(height)
        max_1[0] = height[0]
        max_2 = [None] * len(height)
        max_2[-1] = height[-1]
        
        max_so_far_1, max_so_far_2 = height[0], height[-1]
        for i in range(len(height)):
            max_so_far_1 = max(max_so_far_1, height[i])
            max_so_far_2 = max(max_so_far_2, height[len(height) - 1 - i])
            max_1[i] = max_so_far_1
            max_2[len(height) - 1 - i] = max_so_far_2

        cnt = 0
        for i in range(1, len(height) - 1):
            tmp = min(max_1[i], max_2[i]) - height[i]
            if tmp > 0:
                cnt += tmp
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap(height=[4,2,0,3,2,5]))