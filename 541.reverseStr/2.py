class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result=''
        for i in range(0,len(s),2*k):
            tmp=s[i:i+k]
            tmp=tmp[::-1]+s[i+k:i+2*k]
            result+=tmp
        return result

"""
每2k为一步
把前k个倒序添加
把k-2k个正常添加

注意:一定要把边界问题扔给切片功能自己实现
"""