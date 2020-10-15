class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0

        n = len(nums)

        # 通过双指针，把非0的值都先提到最前面，剩下都是0了
        j = 0
        for i in xrange(n):
            if nums[i]:
                nums[j] = nums[i]
                j += 1

        # 由于剩下都是0了，所以直接在后面赋值就行
        for i in xrange(j, n):
            nums[i] = 0

"""
时间复杂度:O(n)
空间复杂度:O(1)
"""