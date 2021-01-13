class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        maxP = 0
        for i in range(1,n):
            tmp = prices[i] - prices[i-1]
            if tmp >0:
                maxP += tmp
        
        return maxP
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    A = Solution()
    B = A.maxProfit(prices)
    print(B)