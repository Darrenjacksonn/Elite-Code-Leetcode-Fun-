from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        
        # sliding window

        l = 0
        max_profit = 0

        for r in range(len(prices)):

            max_profit = max( max_profit , prices[r] - prices[l] )

            if prices[r] < prices[l]:
                l = r

        return max_profit




sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.max_profit(prices)) # 5

prices = [7,6,4,3,1]
print(sol.max_profit(prices)) # 0

prices = [7,2,9,5,3,6,8,1,9]
print(sol.max_profit(prices)) # 8

prices = [4]
print(sol.max_profit(prices)) # 0