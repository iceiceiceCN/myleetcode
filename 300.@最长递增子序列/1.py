class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) 
                    # 需要与当前的dp[i]对比一下哪个大要哪个，防止被前面的小dp值影响
                    # 参考测试用例[0,1,0,3,2,3]中的dp[3]的变化

        
        return max(dp)

a = Solution()
b = a.lengthOfLIS([0,1,0,3,2,3])

"""
用dp[i]来记录数组nums[:i+1]中最长递增子序列，然后dp[i+1]可以根据dp[:i+1]的值进行判断
如果nums[i+1] > nums[i]，那么就可以根据dp[i]的数值，进行加一

https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
"""