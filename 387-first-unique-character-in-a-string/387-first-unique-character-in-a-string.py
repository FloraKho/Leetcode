class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        return -1