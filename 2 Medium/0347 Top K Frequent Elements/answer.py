from typing import List
from collections import defaultdict


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        # Use defaultdict to store number of occurences of each element
        my_dict = defaultdict(int)
        for item in nums:
            my_dict[item] += 1
        
        # Sort the keys, based on their corresponding values (ie. occurences)
        output = sorted(my_dict , key = lambda x : my_dict.get(x) , reverse = True)

        return output[:k]


# This solution does not satisfies the follow up question, where it asks for a time complexity better than O( n log n).
# Below are the time complexities for each operation:

# nums.sort() -> O(n log n)
# generation of my_dict -> O(n)
# sorted -> O(n log n)
    
# So total as n tends to infinity: O(n log n) exactly.
# To achieve follow up question requirement of lower than O(n log n) [more specifically O(n + k log n)], one would need \n
# to utilize heaps.

sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.top_k_frequent(nums,k)) # [1,2]

nums = [1]
k = 1
print(sol.top_k_frequent(nums,k)) # [1]

nums = [7,-2,-2]
k = 2
print(sol.top_k_frequent(nums,k)) # [-2,7]
