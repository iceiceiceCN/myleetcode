class Solution:
    def spiralOrder(self, matrix):
        x = 0
        y = 0

        # 顺时针方向（右下左上）
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di = 0 # 方向指针
        res = []

        m, n = len(matrix), len(matrix[0])

        for i in range(m*n): # 最多步长 m*n
            res.append(matrix[x][y])

            # 访问过标记为 'v'（‘visited’）
            matrix[x][y] = 'v'

            # 下一步位置
            tx, ty = x + dx[di], y + dy[di]

            # 判断下一步位置是否合理，若合理则更新位置，若不合理则改变方向并更新位置
            if 0 <= tx <= m-1 and 0 <= ty <= n-1 and matrix[tx][ty] != 'v':
                x = tx
                y = ty
            else:
                di = (di+1) % 4
                x += dx[di]
                y += dy[di]

        return res
