class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = -1
        count = 0
        if nums == 1:
            count += 1

        for i in nums:
            if i == 1:
                count += 1
            else:
                maxCount = max(maxCount,count)
                count = 0
        return max(maxCount,count)

"""
 用一个计数器 count 记录 1 的数量，另一个计数器 maxCount 记录当前最大的 1 的数量。
 当我们遇到 1 时，count 加一。
 当我们遇到 0 时：
    将 count 与 maxCount 比较，maxCoiunt 记录较大值。
    将 count 设为 0。
 返回 maxCount
"""