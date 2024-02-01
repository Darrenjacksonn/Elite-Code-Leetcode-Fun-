from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)
        for index in range(1,len(nums)):
            output[index] = output[index - 1] * nums[index - 1]
        
        right_prod = 1

        for index in range(-2, -len(output) - 1 , -1):
            right_prod = nums[index + 1] * right_prod
            output[index] = output[index] * right_prod

        return output




