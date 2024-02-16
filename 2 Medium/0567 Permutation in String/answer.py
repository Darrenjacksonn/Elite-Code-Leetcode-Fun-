from collections import Counter

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:

        # store the characters in s1 as keys in a dict, with their corresponding values being equal \n
        # to their number of occurrences is s1
        my_dict = Counter(s1)

        # will then create a sliding window the width of s1 that moves across s2, at each iteration \n
        # checking if all the characters in s1 match the characters in s2.

        # tracker will go to zero if all the charcters in the window perfectly match s1 (ie. if the \n
        # contains a permutation of s1.)
        tracker = len(s1)
    
        left = 0

        for right in range(len(s2)):
            
            if s2[right] in s1:
                # only adjust tracker if we have not overcounted this character (In other words, tracker \n
                # will not change if this is the 4th occurrence of a letter that is only present in s1 3 times)
                if my_dict[s2[right]] > 0:
                    tracker -= 1
                my_dict[s2[right]] -= 1
            
            if right - left >= len(s1):
                if s2[left] in s1:
                    if my_dict[s2[left]] >= 0:
                        tracker += 1
                    my_dict[s2[left]] += 1
                left += 1
            
            # Check after every iteration if we have a match
            if tracker == 0:
                return True

        return False


        



sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(sol.check_inclusion(s1,s2)) # True

s1 = "ab"
s2 = "eidboaoo"
print(sol.check_inclusion(s1,s2)) # False

s1 = "youbrah"
s2 = "pjebbrahuoylpq"
print(sol.check_inclusion(s1,s2)) # True

s1 = "youbrah"
s2 = "pjebzrahuoylpbq"
print(sol.check_inclusion(s1,s2)) # False

s1 = "cccd"
s2 = "pjeccdchuoylpbq"
print(sol.check_inclusion(s1,s2)) # True

s1 = "hello"
s2 = "ooolleoooleh"
print(sol.check_inclusion(s1,s2)) # False