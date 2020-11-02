class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return [int(i) for i in list(str(int(''.join([str(i) for i in A])) + K))]