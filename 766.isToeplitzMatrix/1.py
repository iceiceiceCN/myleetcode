class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r,row in enumerate(matrix):
            for c,val in enumerate(row):
                if matrix[r-1][c-1] == val or r == 0 or c == 0:
                    continue
                else:return False
        return True
"""
对于对角线上的元素来说，如果当前元素不是第一个出现的元素，那么它前面的元素一定在当前元素的左上角。
可以推出，对于位于坐标 (r, c) 上的元素，
只需要检查 r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c] 就可以了。

时间复杂度: O(M*N)。
空间复杂度: O(1)。
"""