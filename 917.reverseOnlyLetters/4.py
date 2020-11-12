class Solution(object):
    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)

"""
反转指针：

一个接一个输出 s 的所有字符。当遇到一个字母时，我们希望找到逆序遍历字符串的下一个字母。

所以我们这么做：维护一个指针 j 从后往前遍历字符串，当需要字母时就使用它。
"""