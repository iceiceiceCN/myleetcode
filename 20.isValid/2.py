class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1 :
            return False
        
        pairs = {'(':')','{':'}','[':']'}
        stack = list()
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or c != pairs[stack[-1]]:
                    return False
                stack.pop()
        return  not stack
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