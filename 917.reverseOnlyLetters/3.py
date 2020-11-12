class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        
        return "".join(ans)

"""
字母栈方法:
先将字母全部入栈，然后根据指针指向，如果是字母则出栈字母，如果是符号则直接append符号。

看到倒序或反转就要想到【栈】
"""