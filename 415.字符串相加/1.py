class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):  # 保证num1长度大
            num1, num2 = num2, num1
        num2 = '0'*(len(num1)-len(num2)) + num2
        res = ''
        summ = 0
        for i in range(len(num1)):
            n1 = int(num1[-i-1])
            n2 = int(num2[-i-1])
            res = str((n1 + n2 + summ) % 10) + res
            summ = (n1 + n2 + summ)//10

        if summ == 1:
            res = '1' + res
        return res


if __name__ == "__main__":
    A = Solution()
    B = A.addStrings("9", "99")

# 参照67题
"""
遇到字符串相加的题，就用【双指针】
先将两个字符串的长度设置一样，然后逐个相加
"""