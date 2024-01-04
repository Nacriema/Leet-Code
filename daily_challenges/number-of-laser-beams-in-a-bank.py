"""
    Problem statement:
        Anti-theft security devices are activated inside a bank. 
        You are given a 0-indexed binary string array bank representing the floor plan of the bank, 
        which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. 
        '0' means the cell is empty, while'1' means the cell has a security device.

        There is one laser beam between any two security devices if both conditions are met:
            * The two devices are located on two different rows: r1 and r2, where r1 < r2.
            * For each row i where r1 < i < r2, there are no security devices in the ith row.

        Laser beams are independent, i.e., one beam does not interfere nor join with another.
        Return the total number of laser beams in the bank.
"""
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev = None
        for layer in bank:
            n_cam = layer.count("1")
            if n_cam != 0:
                if prev is not None:
                    count += prev * n_cam
                prev = n_cam
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfBeams(bank = ["011001", "000000", "010100", "001000"]))
    print(s.numberOfBeams(bank = ["000", "111", "000"]))
