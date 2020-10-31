class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        x = 0
        y = 1
        
        N = len(A)
        ans = [None] * N
        for i in range(N):
            if A[i]%2 == 0:
                ans[x] = A[i]
                x +=2

        for j in range(N):
            if A[j]%2 == 1:
                ans[y] = A[j]
                y +=2
        return ans
        
"""
遍历一遍数组把所有的偶数放进 ans[0]，ans[2]，ans[4]，依次类推。
再遍历一遍数组把所有的奇数依次放进 ans[1]，ans[3]，ans[5]，依次类推。
260 ms	15.3 MB
"""