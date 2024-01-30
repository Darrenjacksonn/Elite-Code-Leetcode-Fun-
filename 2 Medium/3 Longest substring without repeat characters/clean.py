class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        left = 0

        my_set = set()
        max_length = 1

        for right in range(len(s)):
        
            if s[right] not in my_set:
                max_length = max( max_length , right - left + 1)
            
            else:
                while s[right] in my_set:
                    my_set.remove(s[left])
                    left += 1
                    
            my_set.add(s[right])

        return max_length
