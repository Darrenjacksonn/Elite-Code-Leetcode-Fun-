from typing import List
from collections import defaultdict

class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:

        # Dictionaries to track if a digit is already present in row, col or square
        # Keys = row index , value = set containing all digits already in that row
        # Square keys will be tuple pair of top left indexes in square : ( row_index // 3 , col_index // 3)
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        square_check = defaultdict(set)

        # Iterate over every item in board to check if its valid
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                    
                if item in '.':
                    continue

                if item in row_check[r] or item in col_check[c] or item in square_check[(r // 3 , c // 3)]:
                    return False
    
                row_check[r].add(item)
                col_check[c].add(item)
                square_check[( r // 3 , c // 3 )].add(item)

        return True




sol = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
print(sol.is_valid_sudoku(board)) # True

board = [
    ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.is_valid_sudoku(board)) # False