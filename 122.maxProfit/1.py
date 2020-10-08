prices = [7,6,4,3,1]

class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp>0: profit += tmp

        return profit


if __name__ == "__main__":
    A = Solution()
    B = A.maxProfit(prices)
    print(B)


"""
1.单独交易日：设今天价格P1，明天价格P2，则今天买入、明天卖出可赚取P2-P1
2.连续上涨交易日：设此上涨交易日股票价格分别为P1,P2...Pn,则第一天买最后一天卖收益最大,即Pn-P1;等价于每天都买卖,即Pn-P1=(P2-P1)+(P3-P2)+...+(Pn-Pn-1)
3.连续下降交易日：则不买卖收益最大,即不会亏钱

算法流程：遍历价格列表，所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）
    设 tmp 为第 i-1 日买入与第 i 日卖出赚取的利润，即 tmp = prices[i] - prices[i - 1] ；
    当该天利润为正 tmp > 0，则将利润加入总利润 profit；当利润为 0 或为负，则直接跳过；
    遍历完成后，返回总利润 profit
"""