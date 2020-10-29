class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for i in range((len(row)+1)//2):
                if row[i] == row[-1-i]:
                    row[i] = row[-1-i] = 1-row[i]
        
        return A

"""
首先我们一行的第一个数，找到它对应的数，也就是这一行最后一个
如果这两个数是不同的，比如说一个是1,一个是0,那么先10反转，则一个是0,一个是1,再左右翻转，又变回一个是1,一个是0
这说明当两个数是不同的时候，不用做任何事情
当两个数相同的时候，要同时异或或被1减，即10反转
注意，循环的范围应该是range(len(row) + 1) // 2)，不能忘了加一。
因为，如果列数为奇数，那么中间的数虽然不要左右交换，但是10还是要反转的，因此要多一次循环，相同于中间的数与自己是相同的，要反转。

时间复杂度 O(N)，做了一次遍历。
空间复杂度 O(1)，只用了常量空间，没有用额外的空间
"""