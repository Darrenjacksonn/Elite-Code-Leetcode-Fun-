from typing import List

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Use Backtracking

        # Compute all possible combinations, where repeat digits are allowed, backtrack whenever the sum goes above target.
        # Append the answer if it equals target and is not already in use

        subset = []
        output = []

        def dfs(nums = candidates, iteration = 0, current_sum = 0):

            if current_sum ==  target:
                if subset not in output:
                    output.append(subset[:])
                return
            
            if current_sum > target or iteration >= len(nums):
                return
            
            # Two changes are, add the current element, or add the next element

            # Add the current element
            subset.append(nums[iteration])
            dfs(nums, iteration, current_sum + nums[iteration])

            # Add the next element
            subset.pop()
            dfs(nums, iteration + 1, current_sum)

        dfs()
        return output






sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combination_sum(candidates,target)) # [[2,2,3],[7]]

candidates = [2,3,5]
target = 8
print(sol.combination_sum(candidates,target)) # [[2,2,2,2],[2,3,3],[3,5]]

candidates = [2]
target = 1
print(sol.combination_sum(candidates,target)) # []

candidates = [2]
target = 2
print(sol.combination_sum(candidates,target)) # [[2]]