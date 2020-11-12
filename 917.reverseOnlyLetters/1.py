class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        right = len(S) - 1
        flag = 0
        s = ""
        check = {}
        for i in range(len(S)-1,-1,-1):
            if 65 <= ord(S[i]) <= 90 or 97 <= ord(S[i]) <= 122:
                s += S[i]
            else:
                check[i] = S[i]
        s_list = list(s)

        for key in sorted(check.keys()): # 按顺序遍历符号字典，否则插入符号前后的下标不一样
            s_list.insert(key,check[key])
        s = ''.join(s_list)

        return s
"""
tips:按排序顺序中的键遍历Python字典的方法
1.for key in sorted(D.iterkeys()):
    .. code ..
在Python 3.x中，使用D.keys()（与Python 2.x中的D.iterkeys()相同）

2.假设键/值按顺序插入，则可以使用OrderedDict：
>>> from collections import OrderedDict
>>> d = OrderedDict()
>>> d[1] = 'a'
>>> d[2] = 'a'
>>> d[5] = 'b'
>>> d[7] = 'a'
>>> d
OrderedDict([(1, 'a'), (2, 'a'), (5, 'b'), (7, 'a')])
>>> d.keys()
[1, 2, 5, 7]
"""

if __name__ == "__main__":
    a = Solution()
    b = a.reverseOnlyLetters("a-bC-dEf-ghIj")
    print(b)