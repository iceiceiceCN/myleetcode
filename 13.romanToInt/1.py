class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        INT = 0

        for i in range(len(s)-1): # 最后一个字符不管任何情况都是直接加上
            if Roman[s[i]] >= Roman[s[i+1]]:
                INT += Roman[s[i]]
            else:
                INT -= Roman[s[i]]
        
        return INT + Roman[s[-1]]

"""
只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，且等于右边的字符代表的数减左边字符代表的数。
比如 CM 等于 1000−100，XC 等于 100−10...
"""