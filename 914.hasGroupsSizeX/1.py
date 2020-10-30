from collections import Counter
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = Counter(deck)
        N = len(deck)
        for i in range(2,N+1):
            if N % i ==0:
                if all(v % i ==0 for v in count.values()):
                    return True
        
        return False
"""
暴力枚举
对于每个枚举的X，先判断是否能把deck切分成整数个数组，即判断X是否为N的约数。
然后再判断X是否能把每个数字i的牌划分，即判断X是否为i牌数量的约数。


时间复杂度：O(N^2)，其中 N 是卡牌个数。最多枚举 N 个可能的 X，对于每个 X，要遍历的数字 i 最多有 N 个。

空间复杂度：O(N + C) 或 O(N)，其中 C 是数组 deck 中数的范围，在本题中 C 的值为 10000。
在 C++ 和 Java 代码中，我们先用频率数组 count 存储了每个数字 i 出现的次数 count[i]，随后将所有超过零的次数转移到数组 values 中，方便进行遍历，因此需要使用长度为 C 的 count 数组以及长度不超过 N 的 values 数组，空间复杂度为 O(N + C)。
在 Python 代码中，我们直接使用哈希映射存储每个数字 i 以及出现的次数，因此空间复杂度为 O(N)。
"""