""" 
    Problem statement:
        Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
        Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
        Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

        Example 1:
            Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
            Output: [2,2,2,1,4,3,3,9,6,7,19]

        Example 2:
            Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
            Output: [22,28,8,6,17,44]

        Constraints:
            * 1 <= arr1.length, arr2.length <= 1000
            * 0 <= arr1[i], arr2[i] <= 1000
            * All the elements of arr2 are distinct.
            * Each arr2[i] is in arr1.
"""
from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_cnt = Counter(arr1)
        rs = [0] * len(arr1)
        curr_idx = 0
        for item in arr2:
            for _ in range(arr1_cnt[item]):
                rs[curr_idx] = item
                curr_idx += 1
            del arr1_cnt[item]
        # Fill others 
        for k, v in sorted(arr1_cnt.items(), key=lambda x: x[0]):
            for _ in range(v):
                rs[curr_idx] = k
                curr_idx += 1
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
    print(s.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))