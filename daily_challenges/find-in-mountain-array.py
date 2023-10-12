""" 
    Problem Statement:
        (This problem is an interactive problem)
        You may recall that an array arr is a mountain array if an only if:
            * arr.length >= 3
            * There exist some i with 0 < i < arr.length - 1 such that:
                * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
                * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
                
        Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
        If such an index does not exist, return -1.
        
        You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
            * MountainArray.get(k) returns the elements of the array at index k (0-indexed)
            * MountainArray.length() returns the length of the array.
            
        Submission making more than 100 calls to MountainArray.get() will be judged Wrong Answer. Also, any solutions 
        that attempt to circumvent the judge will result in disqualification.
        
        
        Example 1:
            Input: array = [1,2,3,4,5,3,1], target = 3
            Output: 2
            Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
            
        Example 2:
            Input: array = [0,1,2,4,2,1], target = 3
            Output: -1
            Explanation: 3 does not exist in the array, so we return -1.
            
        Constraints:
            * 3 <= mountain_arr.length() <= 10^4
            * 0 <= target <= 10^9
            * 0 <= mountain_arr.get(index) <= 10^9
            
        Hint:
            Use binary search 3 times
                * Find the peek
                * Find target 
                
        Note: 
            For a given mountainArray, there exist one point i where:
                * arr[0] < arr[1] < ... < arr[i-1] < arr[i] AND arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


# Iterative method for Binary Search
def binary_search(arr, x):
    low_index = 0
    high_index = len(arr) - 1
    mid_index = 0
    
    while low_index <= high_index:
        mid_index = (high_index + low_index) // 2
        
        # If x is greater, ignore left half
        if arr[mid_index] < x:
            low_index = mid_index + 1
        # If x is smaller, ignore right half
        elif arr[mid_index] > x:
            high_index = mid_index - 1
        else:
            # arr[mid_index] == x
            return mid_index
    
    # If we reach here, then the element was not present
    return -1


class MountainArray:
    def __init__(self, arr):
        self.__arr = arr
        self._get_time = 0
    
    def get(self, index: int) -> int:
        self._get_time += 1
        print(f'[INFO] MountainArray get call {self._get_time} times')
        if self._get_time > 100:
            raise Exception('[WARNING] Call more than 100 times, disqualified !!!')
        return self.__arr[index]
    
    def length(self) -> int:
        return len(self.__arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """_summary_

        Args:
            target (int): _description_
            mountain_arr (MountainArray): _description_

        Returns:
            int: _description_
        """
        # Add memo (in case of we call get same index multiple times)
        memo = dict()
        
        def binSearch(mountain, low, high, target, memo):
            increase_branch = False
            if low == 0:
                increase_branch = True
            
            while low <= high:
                mid = (low + high) // 2
                val = memo.get(mid, -1)
                if val == -1:
                    val = mountain.get(mid)
                    memo.update({mid: val})
                
                if val == target:
                    return mid
                
                if increase_branch:
                    if val > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if val > target:
                        low = mid + 1
                    else:
                        high = mid - 1
            return -1
        
        # 1. Find the peak for the current mountain 
        low = 0 
        high = mountain_arr.length() - 1
        peak = 0
        
        while low <= high:
            peak = (high + low) // 2
            # print(f'Mid: {mid}, Low: {low}, High: {high}')
            
            # XXX Bug when peak = 0
            # Check the current value with neighbors
            if peak > 0:
                prev = memo.get(peak - 1, -1)
            else:
                prev = -2
            next = memo.get(peak + 1, -1)
            curr = memo.get(peak, -1)
                        
            if prev == -1:
                prev = mountain_arr.get(peak - 1)
                memo.update({peak - 1: prev})
            if next == -1:
                next = mountain_arr.get(peak + 1)
                memo.update({peak + 1: next})
            if curr == -1:
                curr = mountain_arr.get(peak)
                memo.update({peak: curr})
            
            # 3 cases
            if prev < curr and curr > next:
                break  # This mid is the peak of the array
            elif prev < curr < next:
                # Mean we are on the left side, move the low to mid + 1
                low = peak + 1
            else:
                high = peak - 1
        
        print(f'Memo: {memo}')
        print(f'Find the peak at index: {peak}')
        
        first_found = binSearch(mountain=mountain_arr, low=0, high=peak, target=target, memo=memo)
        second_found = binSearch(mountain=mountain_arr, low=peak, high=mountain_arr.length()-1, target=target, memo=memo)
        
        if first_found == -1:
            if second_found != -1: return second_found
            return -1
        else:
            if second_found == -1:
                return first_found
            else:
                return min(first_found, second_found)
    
    
if __name__ == '__main__':
    s = Solution()
    # print(s.findInMountainArray(target=3, mountain_arr=MountainArray(arr=[1, 2, 3, 4, 5, 3, 1])))
    # print(s.findInMountainArray(target=3, mountain_arr=MountainArray(arr=[0, 1, 2, 4, 2, 1])))
    # print(s.findInMountainArray(target=0, mountain_arr= MountainArray(arr=[3,5,3,2,0])))
    print(s.findInMountainArray(target=0, mountain_arr= MountainArray(arr=[3,5,3,2,0])))

    # print(binary_search(arr=[ 2, 3, 4, 10, 40], x=4))