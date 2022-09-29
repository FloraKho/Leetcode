class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}
        for string in strs:
            sorted_string = ''.join(sorted(string)) #'aet', 'ant', 'abt'
            if sorted_string not in charCount:
                charCount[sorted_string] = [] # charCount = {'aet': [], 'ant': [], 'abt': []}
            charCount[sorted_string].append(string) #charCount = {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        return list(charCount.values()) #charCount.values() -> each list
