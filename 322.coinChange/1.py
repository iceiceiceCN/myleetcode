class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = dict()
        def dp(n):
            if n in memo: return memo[n]

            if n == 0 :return 0
            if n < 0 : return -1
            res = float('INF')

            for coin in coins:
                sub = dp(n-coin)
                if sub == -1: continue
                res = min(res,sub+1)

            memo[n] = res  if res != float('INF') else -1
            return memo[n]

        return dp(amount)


"""
如果不用「备忘录」的话会超时
「备忘录」大大减小了子问题数目，完全消除了子问题的冗余，所以子问题总数不会超过金额数 n，即子问题数目为 O(n)。
处理一个子问题的时间不变，仍是 O(k)，所以总的时间复杂度是 O(kn)。
"""