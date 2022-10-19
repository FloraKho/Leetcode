class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            #sorted
            if nums[left] < nums[right]:
                res = min(res, nums[left]) #leftmost sorted
                #break the while loop
                break
            #not sorted
            mid = (left + right) // 2
            res = min(res, nums[mid])
            
            #check search left or right
            if nums[mid] >= nums[left]: #it means it is part of left portion
                left = mid + 1
            else:
                right = mid - 1
        return res