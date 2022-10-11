class Solution:
    def isPalindrome(self, s:str) -> bool:
        #two pointer
        left, right = 0, len(s) - 1
        while left < right:
            #when left smaller than right and s[left] is not a character
            while left < right and not s[left].isalnum():
                #left will add 1
                left += 1
            #when left smaller than right and s[right] is not a charater
            while left < right and not s[right].isalnum():
                #right will reduce 1
                right -= 1
            #s[left] and s[right] need to conver to lowercase
            #if s[left] is not equal to s[right]
            #return False
            if s[left].lower() != s[right].lower():
                return False
            #if equal, we should continue, and left + 1, right - 1
            left += 1
            right -= 1
        # else return True
        return True