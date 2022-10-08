class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        # {0, 1, 3}
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
        