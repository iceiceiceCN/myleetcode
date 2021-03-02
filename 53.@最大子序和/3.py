class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)

"""
这一段代码我运用了动态规划的思想，在此期间看了很多优秀，精简的算法，然后自己总结出来了这段代码
这段代码首先是一个迭代，从nums[0]到nums[-1]
然后就是总体了,nums[i]是从1开始的，开始算的是num[0]+nums[1]与nums[1]的最大值，
这里这么写可以看成nums[i-1]+nums[i]是看nums[i-1]大于0还是小于0，大于0自然选这个，
小于0的话，相加是要比num[i]小的，所以选择num[i]，这样一直往后迭代，最后返回max(nums),
也就是nums列表的最大值。
"""