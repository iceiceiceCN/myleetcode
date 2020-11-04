class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s

"""
line = "abcde"
line[:-1]
结果为：'abcd'
line[:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分。

line = "abcde"
line[::-1]
结果为：'edcba'
"""