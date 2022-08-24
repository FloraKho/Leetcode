class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First iterate over the array
            # if the current value is 0
            # delete current index and add it to the back
            
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(nums[i])
            