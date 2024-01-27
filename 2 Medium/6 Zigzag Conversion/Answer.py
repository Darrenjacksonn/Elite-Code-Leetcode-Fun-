from typing import List, Optional

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        

        output = [ '' for _ in range(numRows) ]
        # entry_row dictates which row to input character of s. 
        entry_row = 0
        for char in s:

            # direction flips at top and bottom of zigzag pattern
            if entry_row == 0:
                direction = 1
            if entry_row == numRows - 1:
                direction = -1

            output[entry_row] = output[entry_row] + char
            entry_row += direction

        return ''.join(output)





sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s,numRows)) # "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s,numRows)) # "PINALSIGYAHRPI"

s = "A"
numRows = 1
print(sol.convert(s,numRows)) # "A"

s = "ABCDEFGHIJKLMNOP"
numRows = 1
print(sol.convert(s,numRows)) # "ABCDEFGHIJKLMNOP"
