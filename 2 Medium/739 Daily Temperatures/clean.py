from typing import List

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = []

        for i in range( len(temperatures) ):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_index = stack.pop()
                output[old_index] = i - old_index

            stack.append(i)
            
        return output