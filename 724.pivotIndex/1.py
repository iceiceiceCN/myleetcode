class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        for i,num in enumerate(nums):
            ind_sum = sum(nums[:i])
            if ind_sum == S - nums[i] - ind_sum:
                return i
        return -1