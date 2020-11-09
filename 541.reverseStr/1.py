class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res , flag = "", True
        for i in range(0,len(s),k):
            if flag == True:
                res = res + s[i:i+k][::-1]
            else:
                res = res + s[i:i+k]
            flag = not flag
        return res


if __name__ == "__main__":
    A = Solution()
    B = A.reverseStr(s="abcdefg", k=2)
    print(B)

"""
range第三个参数是一个步进，结合那个flag，实现第奇数个k步长翻转，偶数个k步长不翻转。
range最后一段不够k长度的就是实际剩余长度。
Python中的切片操作，选取长度大于实际长度的，按实际长度处理。 比如 s=‘01234’，s[1:999] = ‘1234’。
"""