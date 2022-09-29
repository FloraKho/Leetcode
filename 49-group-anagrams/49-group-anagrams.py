class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}
        for string in strs:
            sorted_string = ''.join(sorted(string)) #'aet'
            if sorted_string not in charCount:
                charCount[sorted_string] = []
            charCount[sorted_string].append(string)
        return list(charCount.values())
