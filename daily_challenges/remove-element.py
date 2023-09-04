"""
    Problem Statement:
        Given an integer array nums and an integer val
        Remove all occurrences of val in nums in-place. The order
        of the elements may be changed. Then return the number of elements in nums which are not equal to val
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Modified the List in-place
        """
        memo = []
        count = 0
        for i, num in enumerate(nums):
            print(f'Memo: {memo}')
            if num == val:
                memo.append(i)
            else:
                count += 1
                if len(memo):
                    if i > memo[0]:
                        nums[memo.pop(0)] = num
                        memo.append(i)
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
    print(s.removeElement(nums=[3,2,2,3], val=3))