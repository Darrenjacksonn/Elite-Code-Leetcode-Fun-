from typing import List
from collections import defaultdict


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        my_dict = defaultdict(int)

        for item in nums:
            my_dict[item] += 1
        
        output = sorted(my_dict , key = lambda x : my_dict.get(x) , reverse = True)

        return output[:k]