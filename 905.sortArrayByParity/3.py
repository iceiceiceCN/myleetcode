class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i , j = 0 , len(A)-1
        while i < j :
            if A[i]%2 > A[j]%2:
                A[i],A[j]=A[j],A[i]

            if A[i]%2 ==0:i+=1
            if A[j]%2 ==1:j-=1
        return A

"""
维护两个指针 i 和 j，
循环保证每刻小于 i 的变量都是偶数（也就是 A[k] % 2 == 0 当 k < i），
所有大于 j 的都是奇数。
"""