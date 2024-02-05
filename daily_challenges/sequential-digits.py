"""
    Problem statement:
        An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
        Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

        Example 1:
            Input: low = 100, high = 300
            Output: [123,234]

        Example 2:
            Input: low = 1000, high = 13000
            Output: [1234,2345,3456,4567,5678,6789,12345]

        Constraints:
            * 10 <= low <= high <= 10^9
"""
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_len = len(str(low))
        high_len = len(str(high))
        start_low = int(str(low)[0])
        
        result = []  # type: list
        
        for lng in range(low_len, high_len + 1):
            print(f'Render number with length: {lng}')
            for pivot in range(1, 10):
                if pivot + lng >= 11:
                    continue
                hint_num = int(''.join(map(str, range(pivot, pivot + lng, 1))))
                if hint_num < low: continue
                if lng == high_len:
                    # Perform checking these value 
                    if hint_num <= high:
                        result.append(hint_num)
                else:
                    result.append(hint_num)
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.sequentialDigits(low = 100, high = 300))
    # print(s.sequentialDigits(low = 1000, high = 13000))
    # print(s.sequentialDigits(low = 10, high = 1000000000))
    # print(s.sequentialDigits(low=58, high=155))
    print(s.sequentialDigits(low=234, high=2314))