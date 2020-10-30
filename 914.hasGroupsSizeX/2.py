from fractions import gcd
from collections import Counter
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        vals = Counter(deck).values()
        return reduce(gcd,vals) >=2 

"""
用fractions的gcd来进行求公约数
用reduce(function, iterable)来返回得到的值，因为vals是iterable，无法直接用gcd()来进行计算
"""