from typing import List

class Solution:
    def longest_consecutive(self, nums: List) -> int:

        my_set = set(nums)
        longest = 0

        for el in my_set:

            if (el - 1) in my_set:
                continue

            counter = 1
            while (el + counter) in my_set:
                counter += 1

            longest = max (longest , counter)

        return longest

