class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos1,pos2 = 0,len(matrix)-1

        while pos1 < pos2:
            add = 0
            while add < pos2 - pos1: # pos2 pos1之间的距离已经走完了 开始内圈循环
                # 经过了add次循环,即pos2-pos1次
                # #左上角为0块，右上角为1块，右下角为2块，左下角为3块

                tmp = matrix[pos2-add][pos1]
                # 2 ->3
                matrix[pos2-add][pos1] = matrix[pos2][pos2-add]

                # 1 ->2
                matrix[pos2][pos2-add] = matrix[pos1+add][pos2]

                # 0 ->1
                matrix[pos1+add][pos2] = matrix[pos1][pos1+add]

                # 3 ->0
                matrix[pos1][pos1+add] = tmp

                add += 1
            pos1+=1
            pos2-=1

a = Solution()
b = a.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#https://leetcode-cn.com/problems/rotate-image/solution/li-kou-48xiao-bai-du-neng-kan-dong-de-fang-fa-zhu-/