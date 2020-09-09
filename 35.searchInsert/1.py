class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        times = 0
        lens = len(nums)
        if target in nums:
            return nums.index(target)
        elif lens == 1:
            if target <= nums[0]:
                return 0
            elif target >= nums[0]:
                return 1
        else:
            for i in range(lens-1):
                if target < nums[i+1] and target > nums[i]:
                    return i+1
                elif target <= nums[0]:
                    return 0
                elif target >= nums[lens-1]:
                    return lens
