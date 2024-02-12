from typing import List

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:

        subset = []
        output = []

        def dfs(nums = candidates, iteration = 0, current_sum = 0):

            if current_sum ==  target:
                if subset not in output:
                    output.append(subset[:])
                return
            
            if current_sum > target or iteration >= len(nums):
                return
            
            subset.append(nums[iteration])
            dfs(nums, iteration, current_sum + nums[iteration])

            subset.pop()
            dfs(nums, iteration + 1, current_sum)

        dfs()
        return output