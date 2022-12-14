class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #index
        
        while left <= right: #binary search requirement
            mid = (left + right) // 2
            #target is equal to nums[mid], return index
            if target == nums[mid]:
                return mid
            #left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    # if target <= nums[mid] or target >= nums[left]
                    right = mid - 1
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1