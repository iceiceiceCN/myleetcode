class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed
        flowerbed = flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                n = n-1
                flowerbed[i] = 1
        return n <= 0

"""
我们从左到右扫描数组 flowerbed，如果数组中有一个 0，并且这个 0 的左右两侧都是 0，
那么我们就可以在这个位置种花，即将这个位置的 0 修改成 1

时间复杂度：O(N)，其中 N 是数组 flowerbed 的长度。
空间复杂度：O(1)。
"""