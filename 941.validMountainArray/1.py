class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        i = 0
        if N < 3:return False # 异常判断

        while i+1<N and A[i]<A[i+1]: # 判断i+1是否越界
            i += 1
        
        if i+1 == N or i==0:return False 
        # 如果一直单调会出现两种情况，一种是递减，i=0。另一种是递增，i+1=N

        while i+1<N and A[i]>A[i+1]:
            i += 1
        
        return i+1==N # 如果能顺利到达最后的位置，则说明符合要求
