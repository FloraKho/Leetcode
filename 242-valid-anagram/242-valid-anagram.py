import collections 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        print(sorted_s)
        print(sorted_t)
        
        if collections.Counter(sorted_s) == collections.Counter(sorted_t):
            return True
        return False