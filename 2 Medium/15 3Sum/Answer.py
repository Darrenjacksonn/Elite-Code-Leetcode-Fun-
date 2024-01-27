from typing import List, Optional

class Solution:
    def three_sum(self, nums: List[int], target = 0) -> List[List[int]]: 
        nums.sort()
        output = []

        # Iterate over every element except last 2
        for index in range(len(nums) - 2):
            
            # Skip repeats
            if index != 0 and nums[index] == nums[index - 1]:
                continue
            
            # Check current from index iteration to end
            left , right = index + 1 , len(nums) - 1


            while left < right:
                answer = nums[index] + nums[left] + nums[right]

                if answer > target:
                    right -= 1
                elif answer < target:
                    left += 1
                else:
                    output.append([nums[index] , nums[left] , nums[right]])

                    # Skip duplicates for left and right 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Continue to look for other pairs that mathc current index iteration
                    left += 1
                    right -= 1
            
        return output





sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.three_sum(nums)) # [[-1,-1,2],[-1,0,1]]

nums = [0,0,0]
print(sol.three_sum(nums)) # [[0,0,0]]

nums = [0,1,1]
print(sol.three_sum(nums)) # []