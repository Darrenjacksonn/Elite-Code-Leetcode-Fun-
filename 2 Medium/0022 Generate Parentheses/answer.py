from typing import List

class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:

        output = []

        # Only call this recursive function if you have an empty output list defined previously
        def recursion(n = n, s = '', open = 0, closed = 0): 
            if len(s) == n * 2:
                return output.append(s)
            
            # Ensures that only half the entries are an open bracket
            if open < n:
                recursion(n,s + '(' , open + 1, closed)
            
            # Ensures that a closed bracket is only added if there exists a corresponding open bracket
            if closed < open:
                recursion(n, s + ')', open, closed + 1)
        
        recursion()

        return output




sol = Solution()
n=1
print(sol.generateParenthesis(n)) # ['()']

n=2
print(sol.generateParenthesis(n)) # ['(())', '()()']

n=3
print(sol.generateParenthesis(n)) # ['((()))', '(()())', '(())()', '()(())', '()()()']

n=4
print(sol.generateParenthesis(n)) # ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', 
                                  # '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']