class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        N = len(A)
        ans = [None] * N

        t = 0
        for i,x in enumerate(A):
            if x%2 ==0:
                ans[t] = x
                t+=2

        t = 1

        for i,x in enumerate(A):
            if x%2 ==1:
                ans[t] = x
                t +=2

        return ans

"""
使用enumerate比使用x[i]要快
180 ms	15 MB
"""