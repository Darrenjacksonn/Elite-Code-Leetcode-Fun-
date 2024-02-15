from typing import List, Optional

class Solution:
    def three_sum(self, nums: List[int], target = 0) -> List[List[int]]: 
        nums.sort()
        output = []

        for index in range(len(nums) - 2):
            
            if index != 0 and nums[index] == nums[index - 1]:
                continue
            
            left , right = index + 1 , len(nums) - 1

            while left < right:
                answer = nums[index] + nums[left] + nums[right]

                if answer > target:
                    right -= 1
                elif answer < target:
                    left += 1
                else:
                    output.append([nums[index] , nums[left] , nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return output