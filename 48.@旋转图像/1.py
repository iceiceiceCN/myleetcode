class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        # 浅拷贝 深拷贝
        # 题目里面直接调用的是原来matrix的地址
        # 如果使用matrix[:] = matrix[::-1] 则可以在原地址上原地修改数值
        # 而使用matrix = matrix[::-1] 是将matrix指向新的地址，指向matrix[::-1]创建的数值
        # 因为matrix不是基础变量类型，函数传的时候传的的地址，直接再赋值不会影响原变量而是创建个新的局部变量

        # print("matrix = matrix[::-1] result :")
        # matrix    = matrix[::-1]

        # print("matrix[:] = matrix[::-1] result :")
        matrix[:] = matrix[::-1]

        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]