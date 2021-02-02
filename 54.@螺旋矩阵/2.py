class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        rowS = 0
        colS = 0

        rowE = len(matrix) - 1
        colE = len(matrix[0]) - 1

        while colS <= colE and rowS <= rowE:
            # if rowS <= rowE: # 右
            for i in range(colS,colE + 1):
                res.append(matrix[rowS][i])
            rowS += 1
            # if colS <= colE: # 下
            for i in range(rowS,rowE + 1):
                res.append(matrix[i][colE])
            colE -= 1

            if rowS <= rowE: # 左 
            # 有时候遍历完之后，rowS > rowE , colS > colE, 还没有结束循环，
            # 但运行上一句 colE -=1 时候，使colS = colE了，到这个for循环时，它们又能开始遍历，就BUG了
                for i in range(colE,colS -1 ,-1): 
                    res.append(matrix[rowE][i])
                rowE -= 1
            
            if colS <= colE: # 上 
            # 同理由于rowE -= 1，使rowS = rowE了，于是也能开始遍历，就BUG了
                for i in range(rowE,rowS -1 ,-1):
                    res.append(matrix[i][colS])
                colS += 1

        return res

t = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = Solution()
b = a.spiralOrder(t)
print(b)