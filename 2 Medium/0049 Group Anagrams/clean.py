from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            my_dict[sorted_word].append(word)
        
        output = []
        for value in my_dict.values():
            output.append(value)

        return output