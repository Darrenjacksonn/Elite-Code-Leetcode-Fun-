from typing import List
from collections import defaultdict

class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:

        row_check = defaultdict(set)
        col_check = defaultdict(set)
        square_check = defaultdict(set)

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