class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = anchor = 0 # ans用来记录最长距离；anchor用来当指针，记录当前序列的开头位置，如果发现非递增，则更新anchor
        for i in range(len(nums)):
            if i and nums[i] <= nums[i-1]: anchor = i 
            ans = max(ans,i-anchor+1)
        return ans

"""
每个（连续）增加的子序列是不相交的，并且每当 nums[i-1]>=nums[i] 时，每个此类子序列的边界都会出现。
当它这样做时，它标志着在 nums[i] 处开始一个新的递增子序列，我们将这样的 i 存储在变量 anchor 中。

例如，如果 nums=[7，8，9，1，2，3]，那么 anchor 从 0 开始（nums[anchor]=7），并再次设置为 anchor=3（nums[anchor]=1）。
无论 anchor 的值如何，我们都会记录 i-anchor+1 的候选答案、子数组 nums[anchor]、nums[anchor+1]、…、nums[i] 的长度，并且我们的答案会得到适当的更新。
"""