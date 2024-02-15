from typing import List

# Iterate through list and use a stack to keep track of the indexes of the temperatures that have not found
# a higher temperature yet (aka. orphan temps). When a higher temp than the most recent orphan is detected
# it works backwards through to find all the previous orphans that are smaller than the current temp

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)

        # Stack to keep a record of the indixes of orphan temps
        stack = []

        for i in range( len(temperatures) ):

            # While the current temp is a match for a previously orphan temp
            while stack and temperatures[i] > temperatures[stack[-1]]:
                old_index = stack.pop()
                output[old_index] = i - old_index

            stack.append(i)
            
        return output





sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.daily_temperatures(temperatures)) # [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30,40,50,60]
print(sol.daily_temperatures(temperatures)) # [1, 1, 1, 0]

temperatures = [30,60,90]
print(sol.daily_temperatures(temperatures)) # [1, 1, 0]

temperatures = [31]
print(sol.daily_temperatures(temperatures)) # [0]