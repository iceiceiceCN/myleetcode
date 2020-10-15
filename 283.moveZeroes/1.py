class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        start = 0
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
                start += 1
        return nums
