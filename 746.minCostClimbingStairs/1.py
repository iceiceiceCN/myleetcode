class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        minCost = n * [0]
        minCost[1] = min(cost[0],cost[1])

        for i in range(2,n):
            minCost[i] = min(minCost[i-1]+cost[i],minCost[i-2]+cost[i-1])

        return minCost[-1]

"""
执行用时：56 ms, 在所有 Python 提交中击败了16.96%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了11.40%的用户

理解题意需要注意两点：
第i级台阶是第i-1级台阶的阶梯顶部。
踏上第i级台阶花费cost[i]，直接迈一大步跨过而不踏上去则不用花费。

到达第i级台阶的阶梯顶部的最小花费，有两个选择：
1.先付出最小总花费minCost[i-1]到达第i级台阶（即第i-1级台阶的阶梯顶部），踏上第i级台阶需要再花费cost[i]，再迈一步到达第i级台阶的阶梯顶部，最小总花费为minCost[i-1] + cost[i])；
2.先付出最小总花费minCost[i-2]到达第i-1级台阶（即第i-2级台阶的阶梯顶部），踏上第i-1级台阶需要再花费cost[i-1]，再迈两步跨过第i级台阶直接到达第i级台阶的阶梯顶部，最小总花费为minCost[i-2] + cost[i-1])；

则minCost[i]是上面这两个最小总花费中的最小值。
minCost[i] = min(minCost[i-1] + cost[i], minCost[i-2] + cost[i-1])。
台阶的数组从0开始计数。可以用-1代表地面，并设cost[-1] = 0。

最小总花费的初始值为：
第0级台阶： minCost[0] = min(cost[-1], cost[0]) = min(0, cost[0]) = 0，
第1级台阶： minCost[1] = min(cost[0], cost[1])。
"""