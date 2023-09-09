"""
    Problem Statement:
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
        DO NOT allocate another 2D matrix and do the rotation.

    Example 1:
        Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
        Output: [[7,4,1],[8,5,2],[9,6,3]]   

    Example 2:
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    Idea: 
        - Spiral loop, for each round, try to find the function that can 

        
    Spiral chain, example n = 4
    (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) 
    -> (1, 3) -> (2, 3) -> (3, 3) 
    -> (3, 2) -> (3, 1) -> (3, 0) ->   

    Better Idea, much more than use spiral:
        - Break the elements from outer size into 4 fragments
        - Replace each fragment with the next other
        - Do the same things till we can not break any more
"""
from typing import List


class Solution:
    # def 

    def rotate(self, matrix: List[List[int]]) -> None:
        k = 0
        l = 0

        m = n = len(matrix)

        while (k < m and l < n):
            # Init the shell here 
            shell_index = []

            for i in range(l, n):
                shell_index.append((k, i))
            
            k += 1

            for i in range(k, m):
                shell_index.append((i, n - 1))

            n -= 1
    
            if (k < m):
    
                for i in range(n - 1, (l - 1), -1):
                    shell_index.append((m - 1, i))
    
                m -= 1
    
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    shell_index.append((i, l))
    
                l += 1

            # When end of a shell, do processing the pixel
            print(f'End of a shell, shell:\n{shell_index}')
            delta = len(shell_index) // 4
            print(f'Delta: {delta}')

            # Draw 4 items at once
            for index, _ in enumerate(shell_index):
                four_indexes = []
                for time in range(4):
                    if index + time * delta > len(shell_index) - 1:
                        four_indexes = []
                        break
                    else:
                        four_indexes.append(index + time * delta)

                if len(four_indexes) == 4:
                    # We got the items here
                    print(f'Got items: {four_indexes}')
                    # Exchange the values between items
                    
                    # Swap index with 0 - 3
                    p, q = shell_index[four_indexes[0]] 
                    r, s = shell_index[four_indexes[3]]
                    matrix[p][q], matrix[r][s] =  matrix[r][s], matrix[p][q]

                    p, q = shell_index[four_indexes[1]] 
                    r, s = shell_index[four_indexes[3]]
                    matrix[p][q], matrix[r][s] =  matrix[r][s], matrix[p][q]

                    p, q = shell_index[four_indexes[2]] 
                    r, s = shell_index[four_indexes[3]]
                    matrix[p][q], matrix[r][s] =  matrix[r][s], matrix[p][q]

        return matrix


if __name__ == '__main__':
    s = Solution()
    print()
    print(s.rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    print(s.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]]))

