class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        temp = int(1e9)
        minprice = temp
        maxprofit = 0
        # 遍历的同时寻找最小买价，使计算中买价必然先于卖价，然后用当前价格减去最小买价，从而寻找最大的利润
        for price in prices:
            maxprofit = max(maxprofit,price-minprice)
            minprice = min(price,minprice)
        return maxprofit