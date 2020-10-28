class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:return 0
        nums_copy = nums[:]
        nums_copy.sort()
        if nums_copy[-1] >= 2*nums_copy[-2]:
            return nums.index(nums_copy[-1])
        else:return -1


"""
判断最大数是否为第二大数的两倍
如果最大数必须是所有元素的至少两倍大，那么最大数一定是第二大数的至少两倍大。因此：

找出最大数和第二大数
比较两者大小
"""