class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        # sliding window technique

        # Use a set to keep track of letters already in the window.

        my_set = set()

        left, right, max_substring = 0, 0, 0

        while right < len(s):
            
            # If a letter repeats, move left pointer until it no longer repeats
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            # Add right most char to the set
            my_set.add(s[right])
            right += 1

            # Check if we have a new max substring
            max_substring = max(max_substring, right - left)
  
        return max_substring


sol = Solution()
s = "abcabcbb"
print(sol.length_of_longest_substring(s)) # 3

s = "bbbbb"
print(sol.length_of_longest_substring(s)) # 1

s = "pwwkew"
print(sol.length_of_longest_substring(s)) # 3

s = ""
print(sol.length_of_longest_substring(s)) # 0

s = "x"
print(sol.length_of_longest_substring(s)) # 1