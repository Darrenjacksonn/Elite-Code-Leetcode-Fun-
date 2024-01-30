class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        # Initiate sliding window index
        left = 0

        # Set to keep track of repeat characters
        my_set = set()
        max_length = 1

        for right in range(len(s)):
            
            # If susbtring does not contain repeat characters, check if it is a new max length substring
            if s[right] not in my_set:
                max_length = max( max_length , right - left + 1)
            
            # If it does contain repeat characters, move left closer to right until it doesn't anymore
            else:
                while s[right] in my_set:
                    my_set.remove(s[left])
                    left += 1
                    
            my_set.add(s[right])

        return max_length





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