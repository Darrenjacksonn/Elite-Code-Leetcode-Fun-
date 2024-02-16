from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operator_mapping = {
            '+' : lambda x,y : x + y,
            '-' : lambda x,y : x - y,
            '*' : lambda x,y : x * y,
            '/' : lambda x,y : int(x / y)
        }

        for elem in tokens:
            if elem not in '+-*/':
                stack.append(int(elem))
            else:
                second, first = stack.pop(), stack.pop()
                stack.append(operator_mapping[elem](first,second))

        return stack.pop()