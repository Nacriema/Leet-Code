"""
    Given an integer array of size n, find all elements that appear mode than [n/3] times.

    Example 1:
        Input: nums = [3,2,3]
        Output: [3]

    Example 2:
        Input: nums = [1]
        Output: [1]

    Example 3:
        Input: nums = [1,2]
        Output: [1,2]

    Constraints:
        * 1 <= nums.length < 5 * 10^4
        * -10^9 <= nums[i] <= 10^9

    Follow up: Could you solve the problem in linear time and O(1) space ?

    Note: O(1) space means that the space required by the algorithm to process data is CONSTANT; it does not grow with the 
    size of the data on which the algorithm is operating.

    Hint: How many majority elements could it possibly have ?
    Answer: Majority means number of elements > (n // 3) -> Maximum we have 2 distinct elements
"""
from typing import List


class Solution:
    def majorityElement_idea1(self, nums: List[int]) -> List[int]:
        # Linear time solution first O(n), one loop, but not O(1) space
        limit = len(nums)//3
        table = dict()
        rs = set()
        for num in nums:
            val = table.get(num, 0) + 1
            if val > limit:
                rs.add(num)
                if len(rs) == 2:
                    return list(rs)
            else:
                table[num] = val
        return list(rs)
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        """ Booyer-Moore Voting Algorithm """
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement(nums=[3, 2, 3]))
    print(s.majorityElement(nums=[1]))
    print(s.majorityElement(nums=[1, 2]))
    print(s.majorityElement(nums=[2, 2]))