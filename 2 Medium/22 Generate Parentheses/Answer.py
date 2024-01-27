from typing import List, Optional

class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:

        output = []

        # Only call this recursive function if you have an empty output list defined previously
        def recursion(n,s='',left=0,right=0): 
            if len(s) == n*2:
                return output.append(s)
            
            # Ensures that only half the entries are an open bracket
            if left < n:
                recursion(n,s + '(' , left + 1, right)
            
            # Ensures that a closed bracket is only added if there exists a corresponding open bracket
            if right < left:
                recursion(n, s + ')', left, right + 1)
        
        recursion(n)

        return output




sol = Solution()
n=1
print(sol.generateParenthesis(n))

n=2
print(sol.generateParenthesis(n))

n=3
print(sol.generateParenthesis(n))

n=4
print(sol.generateParenthesis(n))