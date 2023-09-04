"""
    Problem Statement:
        Write a program to solve a Sudoku puzzle by filling the empty cells.
        A sudoku solution must satisfy all of the following rules:
            1. Each of the digits 1-9 must occur exactly once in each row
            2. Each of the digits 1-9 must occur exactly once in each column
            3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid
        The "." character indicates empty cells.

    Example 1:
        Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
        
    Constrains:
        * board.length == 9
        * board[i].length == 9
        * board[j][j] is a digit or "."
        * it is guaranteed that the input board has only one solution
"""
from typing import List
from itertools import product


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
            Do not return anything, modify boad in-place instead.

            Use Algorithm X - Exact cover problem to solve this
        """
        def convert(X, Y):
            """
                Convert problem
            """
            X = {j: set() for j in X}
            for i, row in Y.items():
                for j in row:
                    X[j].add(i)
            return X, Y

        # Algorithm X core
        def solve(X, Y, solution):
            if not X:
                yield list(solution)
            else:
                c = min(X, key=lambda c: len(X[c]))
                for r in list(X[c]):
                    solution.append(r)
                    cols = select(X, Y, r)
                    for s in solve(X, Y, solution):
                        yield s
                    deselect(X, Y, r, cols)
                    solution.pop()

        def select(X, Y, r):
            cols = []
            for j in Y[r]:
                for i in X[j]:
                    for k in Y[i]:
                        if k != j:
                            X[k].remove(i)
                cols.append(X.pop(j))
            return cols

        def deselect(X, Y, r, cols):
            for j in reversed(Y[r]):
                X[j] = cols.pop()
                for i in X[j]:
                    for k in Y[i]:
                        if k != j:
                            X[k].add(i)

        R, C = 3, 3  # Type 3 x 3 Sudoku grid
        N = R * C

        # Construct the problem
        X = ([("rc", rc) for rc in product(range(N), range(N))] +
            [("rn", rn) for rn in product(range(N), range(1, N + 1))] + 
            [("cn", cn) for cn in product(range(N), range(1, N + 1))] +  
            [("bn", bn) for bn in product(range(N), range(1, N + 1))])  

        Y = dict()
        for r, c, n in product(range(N), range(N), range(1, N + 1)):
            b = (r // R) * R + (c // C) # Block Box number
            Y[(r, c, n)] = [
                ("rc", (r, c)),
                ("rn", (r, n)),
                ("cn", (c, n)),
                ("bn", (b, n))]
    
        X, Y = convert(X, Y)

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n != ".": 
                    # Not empty cell
                    select(X, Y, (i, j, int(n)))
        
        for solution in solve(X, Y, []):
            for (r, c, n) in solution:
                board[r][c] = N
        
        # Check the length of solution is one
        for i, j, n in solution:
            board[i][j] = str(n)

        return board

if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku(board=[["5","3",".",".","7",".",".",".","."],
                                ["6",".",".","1","9","5",".",".","."],
                                [".","9","8",".",".",".",".","6","."],
                                ["8",".",".",".","6",".",".",".","3"],
                                ["4",".",".","8",".","3",".",".","1"],
                                ["7",".",".",".","2",".",".",".","6"],
                                [".","6",".",".",".",".","2","8","."],
                                [".",".",".","4","1","9",".",".","5"],
                                [".",".",".",".","8",".",".","7","9"]]))
    pass