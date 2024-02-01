from typing import List

class Solution:
    def longest_consecutive(self, nums: List) -> int:

        # Converting to a set has time complexity O(n). We do this as look up's in sets have O(1) time complexity
        my_set = set(nums)

        # Track the longest consecutive elements
        longest = 0

        # This for loop will also have a time complexity of O(n)
        for el in my_set:

            # This is a crucial step for ensuring O(1) complexity, if a number one below the current element exists \n
            # then this element is not the START of a sequence of consecutive numbers and it skips over the element.
            # This excludes any redundant checks in the following while loop
            if (el - 1) in my_set:
                continue
            
            # After finding the start of a consecutive sequence, it loops over that sequence to see how long it is.
            # This can have at most O(n) time complexity.
            counter = 1
            while (el + counter) in my_set:
                counter += 1

            longest = max (longest , counter)

        return longest


# Therefore, this algorithm has a time complexity of O(3n) which is O(n) for large n.



sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longest_consecutive(nums)) # 4

nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longest_consecutive(nums)) # 9

nums = []
print(sol.longest_consecutive(nums)) # 0

nums = [-109]
print(sol.longest_consecutive(nums)) # 1

nums = [6,6]
print(sol.longest_consecutive(nums)) # 1