""" 
    Problem statement:
        Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the bellow
        images.

        Example 1:
            Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [1,4,2,7,5,3,8,6,9]
        
        Example 2:
            Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
            Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        
        Constraints:
            * 1 <= nums.length <= 10^5
            * 1 <= nums[i].length <= 10^5
            * 1 <= sum(nums[i].length) <= 10^5
            * 1 <= nums[i][j] <= 10^5

        Hints:
            * Notice that numbers with equal sums of row and column indexes belong to the same diagonal
            * Store them in tuple (sum, row, val), sort them, and then re group the answer
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        lst = list()
        for row in range(len(nums)):
            for i in range(len(nums[row])):
                lst.append((row + i, row, nums[row][i]))
        
        lst = sorted(lst, key=lambda x: (x[0], -x[1]))
        rs = [_[2] for _ in lst]
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder(nums=[[1,2,3],[4,5,6],[7,8,9]]))
    print(s.findDiagonalOrder(nums=[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))

    # (0, 0) -> (1, 0) -> (0, 1) -> (2, 0) -> (1, 1) -> (0, 2) -> (3, 0)
