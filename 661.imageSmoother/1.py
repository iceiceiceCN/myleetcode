class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R , C = len(M),len(M[0])
        ans = [[0] * C for _ in M] # 初始化ans！

        for r in xrange(R): # xrange比range速度快一些，无脑用吧就
            for c in xrange(C):
                count = 0
                for nr in (r-1,r,r+1):
                    for nc in (c-1,c,c+1):
                        if 0 <= nr < R and 0 <= nc < C: # R和C是行数和列数，所以nr,nc达不到R和C，最多为R-1,C-1
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count
        return ans

"""
对于矩阵中的每一个单元格，找所有 9 个包括它自身在内的紧邻的格子。
然后，我们要将所有邻居的和保存在 ans[r][c] 中，同时记录邻居的数目 count。最终的答案就是和除以邻居数目。
"""