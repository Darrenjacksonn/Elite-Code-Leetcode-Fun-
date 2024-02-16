from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # use a stack to keep track of previous 2 numbers on list that next operator will act on
        stack = []

        # map the operator notation to their respective python operations
        operator_mapping = {
            '+' : lambda x,y : x + y,
            '-' : lambda x,y : x - y,
            '*' : lambda x,y : x * y,
            '/' : lambda x,y : int(x / y)
        }

        # loop over elements
        for elem in tokens:
            # Append element to stack if they are integers
            if elem not in '+-*/':
                stack.append(int(elem))
            # Apply operation to previous two elements
            else:
                second, first = stack.pop(), stack.pop()
                # Add the resultant integer back to the end of the stack
                stack.append(operator_mapping[elem](first,second))

        # The answer is the last element left on the stack
        return stack.pop()




sol = Solution()
tokens = ["2","1","+","3","*"]
print(sol.evalRPN(tokens)) # 9

tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens)) # 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens)) # 22