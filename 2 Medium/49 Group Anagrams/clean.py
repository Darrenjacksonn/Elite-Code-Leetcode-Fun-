from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for string in strs:
            sorted_str = ''.join(sorted(string))
            my_dict[sorted_str].append(string)
        
        output = []
        for key in my_dict:
            output.append(my_dict.get(key))

        return output