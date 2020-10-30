class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda x:x%2)
        return A


"""
使用排序算法，按照模 2 的结果排序

时间复杂度：O(NlogN)，其中 N 是 A 的长度。
空间复杂度：排序空间为 O(N)，取决于内置的 sort 函数实现
"""