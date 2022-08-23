class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, value in enumerate(s):
            if(s.count(value) == 1):
                return index
        return -1
            