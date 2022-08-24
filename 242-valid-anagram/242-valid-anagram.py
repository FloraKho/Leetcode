import collections 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        if collections.Counter(s) == collections.Counter(t):
            return True
        return False