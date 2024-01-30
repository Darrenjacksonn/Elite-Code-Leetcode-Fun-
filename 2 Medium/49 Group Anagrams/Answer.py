from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        
        # This dict will have the string sorted alphabetically as its keys, and a list of its anagrams as values
        my_dict = defaultdict(list)

        # Sort every string and add the sorted version to the key of a dictionary, if the key already exists, the string is \n
        # an anagram with another string that matches this key, so append to this keys corresponding value list.
        for string in strs:
            sorted_str = ''.join(sorted(string))
            my_dict[sorted_str].append(string)
        
        # Convert the values of the dict into an output list
        output = []
        for key in my_dict:
            output.append(my_dict.get(key))

        return output



sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.group_anagrams(strs))

strs = [""]
print(sol.group_anagrams(strs))

strs = ["a"]
print(sol.group_anagrams(strs))