class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = float('-inf')
        # 遍历的同时寻找最小买价，使计算中买价必然先于卖价，然后用当前价格减去最小买价，从而寻找最大的利润
        for price in prices:
            minprice = min(price, minprice) # 找到最低价
            maxprofit = max(maxprofit, price-minprice) # 找到最高利润
        return maxprofit
