from typing import List, Optional

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0 for _ in range(len(temperatures))]
        stack = []
        
        for index, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                output[stack[-1]] = index - stack[-1]
                stack.pop()
            
            stack.append(index)

        return output