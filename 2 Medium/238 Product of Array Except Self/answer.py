from typing import List

# This solution solves the follow up problem, excluding the output array (which has space complexity of O(n)) \n
# it's extra space complexity is O(1), which is the right_prod variable
# It achieves this by first computing an array of left products and then updating that array in place with the \n
# right products.

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:

        # Work out left products
        output = [1] * len(nums)
        for index in range(1,len(nums)):
            output[index] = output[index - 1] * nums[index - 1]
        
        # O(1) extra sapce complexity -> This keeps track of right products at the point
        right_prod = 1

        # Iterate backwards through output array
        for index in range(-2, -len(output) - 1 , -1):
            right_prod = nums[index + 1] * right_prod
            output[index] = output[index] * right_prod

        return output





sol = Solution()
nums = [1,2,3,4]
print(sol.product_except_self(nums)) # [24, 12, 8, 6]

nums = [-1,1,0,-3,3]
print(sol.product_except_self(nums)) # [0, 0, 9, 0, 0]

nums = [0,0]
print(sol.product_except_self(nums)) # [0, 0]

nums = [-1,1]
print(sol.product_except_self(nums)) # [1, -1]