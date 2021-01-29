class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '{': '}', '[': ']'}

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in dic:
                stack.append(dic[i])
            else:
                if not stack or i != stack[-1]:  # 跳出循环的条件：1.栈为空；2.括号不匹配
                    return False
                stack.pop()

        return not stack


"""
奇数数量的长度肯定不符合要求
把括号做成字典dict
然后用栈的方式来模拟

如果是左括号，则入栈append。
如果是 不对应的右括号 或者 此时stack已经空了，则返回False；否则正常出栈pop。
直到把s中所有字符都遍历完，判断此时stack是否为空，返回True/False
"""


if __name__ == "__main__":
    A = Solution()
    B = A.isValid("()[]{}")
    print(B)
