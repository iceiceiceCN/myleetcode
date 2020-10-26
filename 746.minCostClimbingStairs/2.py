class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        minCost0 = 0
        minCost1 = min(cost[0],cost[1])

        for i in range(2,n):
            minCost = min(minCost1+cost[i],minCost0+cost[i-1]) # 这里得到了迈上第2级台阶的最小花费
            minCost0 , minCost1 = minCost1 , minCost # 第1级台阶的最小花费->minCost0 第2级台阶的最小花费->minCost1 然后以此类推

        return minCost

"""
执行用时：36 ms, 在所有 Python 提交中击败了96.71%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.26%的用户

空间利用上可以再优化一下。只用两个变量保存状态转移方程中前面的两个记录，并不断更新，就可以递推下去，这样空间复杂度就由O(N)变为O(1)了
"""