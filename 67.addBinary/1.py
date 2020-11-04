class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 调整a,b长度，使len(a)>len(b)
        if len(a) < len(b):
            a, b = b, a
        
        # 补齐 0
        b = '0'*(len(a)-len(b)) + b
        res = ''
        summ = 0 # 进位值
        for i in range(len(a)):
            # 通过对应位相加 再加上进位值 之后取余2 得到该位计算结果
            res = str((int(a[-i-1])+int(b[-i-1])+summ) % 2) + res
            # 通过对应位相加 再加上进位值 之后整除2 得到下一位的进位值
            summ = (int(a[-i-1])+int(b[-i-1])+summ)//2
        
        # 如果计算到第一位发现仍然有进位值，则在首位加'1'
        if summ == 1:
            res = '1' + res
        return res
