class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)


"""
动态规划解法【重点】
https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
"""

# 空间优化版本
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(nums[i] + pre, nums[i]) # 相当于代替了判断num[i]大于小于0的情况
            res = max(pre, res) # 相当于代替了max(dp)的情况

        return res
