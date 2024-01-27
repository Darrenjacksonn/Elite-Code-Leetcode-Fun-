from typing import List, Optional

# Iterate through list and use a stack to keep track of the indexes of the temperatures that have not found
# a higher temperature yet (aka. orphan temps). When a higher temp than the most recent orphan is detected
# it works backwards through to find all the previous orphans that are smaller than the current temp

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0 for _ in range(len(temperatures))]
        
        # Stack to keep a record of the indixes of orphan temps
        stack = []
        
        for index, temp in enumerate(temperatures):

            # While the current temp is a match for a previously orphan temp
            while stack and temp > temperatures[stack[-1]]:
                output[stack[-1]] = index - stack[-1]
                stack.pop()
            
            stack.append(index)

        return output




# Test the solution 

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))
# [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30,40,50,60]
print(sol.dailyTemperatures(temperatures))
# [1, 1, 1, 0]

temperatures = [30,60,90]
print(sol.dailyTemperatures(temperatures))
# [1, 1, 0]

temperatures = [31]
print(sol.dailyTemperatures(temperatures))
# [0]