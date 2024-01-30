from typing import List, Optional

class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        output = []

        def recursion(n,s='',left=0,right=0): 
            if len(s) == n*2:
                return output.append(s)
            
            if left < n:
                recursion(n,s + '(' , left + 1, right)
            
            if right < left:
                recursion(n, s + ')', left, right + 1)
        
        recursion(n)

        return output