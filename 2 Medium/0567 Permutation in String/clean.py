from collections import Counter

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:

        my_dict = Counter(s1)
        tracker = len(s1)
        left = 0

        for right in range(len(s2)):

            if s2[right] in s1:
                if my_dict[s2[right]] > 0:
                    tracker -= 1
                my_dict[s2[right]] -= 1
            
            if right - left >= len(s1):
                if s2[left] in s1:
                    if my_dict[s2[left]] >= 0:
                        tracker += 1
                    my_dict[s2[left]] += 1
                left += 1
            
            if tracker == 0:
                return True

        return False