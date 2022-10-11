class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #a list of numbers
        #the end of range is the length of numbers
        #find the missing number within the range
        #using set() method to convert with disctinct elements
        #using for...in... method
        #if the number is not in set
        #return missing number
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number