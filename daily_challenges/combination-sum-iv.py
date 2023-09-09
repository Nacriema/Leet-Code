"""
    Problem statement:
        Given an array of distinct images nums and a target number target, return the number of possible combinations that add up to target.
        The test cases are generated so that the answer cat fit in a 32-bit integer

    Example 1:
        Input: nums = [1,2,3], target = 4
        Output: 7
        Explanation:
            The possible combination ways are:
            (1, 1, 1, 1)
            (1, 1, 2)
            (1, 2, 1)
            (1, 3)
            (2, 1, 1)
            (2, 2)
            (3, 1)
            Note that different sequences are counted as different combinations. (like 1,1,2 and 2,1,1 are difference)

    Example 2:
        Input: nums = [9], target = 3
        Output: 0

    Constraints:
        * 1 <= nums.length <= 200
        * 1 <= nums[i] <= 1000
        * All the elements of nums are unique.
        * 1 <= target <= 1000

    Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

    Humm, this problem lead me to the hell. DP Again =)))
    
"""
from typing import List
from itertools import product
import math
from functools import reduce


class Solution:
    def TLE_combinationSum4(self, nums: List[int], target: int) -> int:
        """
            Implemenatation here
            
            Idea:
                - Like a loop, inside each loop, we find all possible solution for this
                - Next loop, we drop the first index of the nums array, like [1, 2, 3], then [2, 3] and final [3] ...
                    - This will reduce the time since we already found the same solution before (like 1, 1, 2 -> Then we can count the another solution)

                Note: May be this idea is not good for now :<
                So we need to counter all possible solution

            We can ignore the num inside nums that has value greater than the target
        """
        nums = sorted(nums)
        print(f'Sorted num: {nums}')

        # Backtracking
        candidates = []  # Contains all possible solutions
        solutions = []  # Store all completed solution

        # Init the base for candidates
        for num in nums:
            if num <= target:
                candidates.append([num])
        
        # print(f'Prepared candidate: {candidates}')

        while len(candidates):
            print(f'Last append candidates: {candidates[-1]}')
            # Make new candidate, by looping all items inside the for loop
            candidate = candidates.pop()
            
            if sum(candidate) == target:
                solutions.append(candidate)
                continue

            for num in nums:
                if num < target - sum(candidate):
                    candidates.append(candidate + [num])
                if num == target - sum(candidate):
                    solutions.append(candidate + [num])
                if num > target - sum(candidate):
                    break
            
        print(f'Solutions: {solutions}')
        return len(solutions)

    def TLE_again_combinationSum4(self, nums: List[int], target: int) -> int:
        """
            Given the nums then find the difference combinations of weights for each num that can sum up the target
            Due to the nums are distinct, then for each solution we can find the number of ways to represent it

            Examples:
                [1, 2, 3] and 4
                We can have the weights (4, 0, 0), (2, 1, 0), (1, 0, 1), (0, 2, 0)
        """
        def compute(combination):
            numerator = math.factorial(sum(combination))
            denumerator = reduce(lambda x, y: x * y, [math.factorial(_) for _ in combination])
            return int(numerator / denumerator)

        # Can I limit the loop range, yes, just by (target // nums[i] + 1)
        
        # 1. Construct the limited
        limits = [(0, target // num + 1, 1) for num in nums]
        print(f'Limits: {limits}')
        # print(f'Limit for each number: {limits}')
        
        # This what I want
        # Ref: https://stackoverflow.com/questions/38068669/dynamic-for-loops-in-python
        combinations = []

        for values in product(*(range(*b) for b in limits)):
            val = 0
            # print(f'Values: {values}')
            for num, weight in zip(nums, values):
                val += num * weight
            if val == target:
                combinations.append(values)
        
        print(f'Combinations: {combinations}')
        # Applied the math to compute real permutation here !!!
        rs = 0
        for comb in combinations:
            rs += compute(combination=comb)
        return rs
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
            Must be solved by using DP :< so sad
        """
        # DP is the possible combination that we can have for each target by the given nums
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            # Finding the number of combination for each target i by given the nums
            for num in nums:
                if i - num >= 0:
                    # This mean we can combine this num with the previous set at target [i - num]
                    dp[i] += dp[i - num]
                    print(f'Adjust DP: {dp}')
        
        return dp[target]



if __name__ == '__main__':
    # Just pass 6/15 case

    s = Solution()
    print(s.combinationSum4(nums=[1, 2, 3], target=3))
    # print(s.combinationSum4(nums=[9], target=3))
    # print(s.combinationSum4(nums= [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], target=10)) # Expected 9
    # print(s.combinationSum4(nums = [4, 2, 1], target=20))

    # TLE Again (just pass 11/15)
    # print(s.combinationSum4(nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100],
    #                         target=31))

