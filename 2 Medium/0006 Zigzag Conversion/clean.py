from typing import List, Optional

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        output = [ '' for _ in range(numRows) ]
        entry_row = 0

        for char in s:

            if entry_row == 0:
                direction = 1
            if entry_row == numRows - 1:
                direction = -1

            output[entry_row] = output[entry_row] + char
            entry_row += direction

        return ''.join(output)