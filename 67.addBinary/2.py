class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
        # 因为bin返回的值中有两位的前缀，所以要从下标2开始取

"""
class int(x, base=10)
x -- 字符串或数字。
base -- 进制数，默认十进制。
int('12',16) -> 18
int('0xa',16) -> 10
int('10',8) -> 8



bin(x)
x -- int 或者 long int 数字
bin() 返回一个整数 int 或者长整数 long int 的二进制表示
bin(10) ->
'0b1010'
bin(20) ->
'0b10100'
"""