class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        my_set = set()

        left, right, max_substring = 0, 0, 0

        while right < len(s):
            
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            
            my_set.add(s[right])
            right += 1

            max_substring = max(max_substring, right - left)
  
        return max_substring
