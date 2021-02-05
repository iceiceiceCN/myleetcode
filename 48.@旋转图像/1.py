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


"""
本题是「旋转二维数组」，如果是「旋转一维数组」呢？
给定一个长度为 n 的一维数组，将前 k 个数移动到末尾。要求 原地 操作，该如何实现?

输入: 1, 2, 3, 4, 5, 6, 7
输出: 4, 5, 6, 7, 1, 2, 3

实现方法：
    1.前 k 个原地翻转
    2.后 n - k 个原地翻转
    3.整体原地翻转

1, 2, 3, 4, 5, 6, 7

前 k 个原地翻转：
3, 2, 1, 4, 5, 6, 7

后 n - k 个原地翻转：
3, 2, 1, 7, 6, 5, 4

整体原地翻转：
4, 5, 6, 7, 1, 2, 3

链接：https://leetcode-cn.com/problems/rotate-image/solution/ji-qiao-ti-zai-zeng-song-yi-wei-xing-shi-377z/
"""