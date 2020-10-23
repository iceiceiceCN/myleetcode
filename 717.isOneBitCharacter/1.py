class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) -1:
            i += bits[i] + 1
        
        if i == len(bits) -1:
            return True
        else:
            return False

"""
方法一：线性扫描
我们可以对 bits 数组从左到右扫描来判断最后一位是否为一比特字符。
当扫描到第 i 位时，如果 bits[i]=1，那么说明这是一个两比特字符，将 i 的值增加 2。
如果 bits[i]=0，那么说明这是一个一比特字符，将 i 的值增加 1。

如果 i 最终落在了 bits.length−1 的位置，那么说明最后一位一定是一比特字符。

时间复杂度：O(n)，其中 n 是 bits 数组的长度。
空间复杂度：O(1)。
"""