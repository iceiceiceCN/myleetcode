class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N):
        cache = {0:0, 1:1}

        for i in range(2,N+1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[N]

"""
记忆化自底向上的方法：
自底向上通过迭代计算斐波那契数的子问题并存储已计算的值，通过已计算的值进行计算。减少递归带来的重复计算。
如果 N 小于等于 1，则返回 N。
迭代 N，将计算出的答案存储在数组中。
使用数组前面的两个斐波那契数计算当前的斐波那契数。
知道我们计算到 N，则返回它的斐波那契数

时间复杂度：O(N)。
空间复杂度：O(N)，使用了空间大小为 N 的数组。
"""