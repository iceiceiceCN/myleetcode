class Solution(object):
    def maxProfit(self, prices):
        ans = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                ans = max(ans,prices[j]-prices[i])
        return ans

# 暴力遍历会超时