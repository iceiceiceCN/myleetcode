class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = []
        for i in str:
            if 65<=ord(i)<=90:
                s.append(chr(ord(i)+32))
            else:
                s.append(i)
        
        return "".join(s)

"""
'A' - 'Z' 对应的 ascii 是 65 - 90；
'a' - 'z' 对应的 ascii 是 97 - 122；
大小字母转换相差32，解题只要记住ord(),chr()函数即可
"""