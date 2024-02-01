from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        
        # sliding window

        left = 0
        max_profit = 0

        for price in prices:
            max_profit = max( max_profit , price - prices[left] )
            
            while price < prices[left]:
                left += 1

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