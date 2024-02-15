from typing import List

class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:

        output = []

        def recursion(n = n, s = '', open = 0, closed = 0): 
            if len(s) == n * 2:
                return output.append(s)
            
            if open < n:
                recursion(n,s + '(' , open + 1, closed)
            
            if closed < open:
                recursion(n, s + ')', open, closed + 1)
        
        recursion()

        return output