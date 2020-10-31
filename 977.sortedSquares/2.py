class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        mid = -1

        for i in range(N):
            if A[i]<0:mid = i

        i = mid
        j = mid+1
        ans = []

        while j<N or i>=0:
            if i<0:
                ans.append(A[j]*A[j])
                j+=1
            elif j==N:
                ans.append(A[i]*A[i])
                i-=1
            elif A[j]*A[j] < A[i]*A[i]:
                ans.append(A[j]*A[j])
                j+=1
            else:
                ans.append(A[i]*A[i])
                i-=1
        return ans

