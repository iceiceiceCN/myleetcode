class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '{': '}', '[': ']', '?': '?'}
        stack = ['?']

        for c in s:
            if c in dict:
                stack.append(c)
            else:
                if c != dict[stack.pop()]:
                    return False
        return len(stack) == 1


"""
流程：
如果 c 是左括号，则入栈 push；
否则通过哈希表判断括号对应关系，若 stack 栈顶出栈括号 stack.pop() 与当前遍历括号 c 不对应，则提前返回 false。


边界问题：
栈 stack 为空：此时 stack.pop() 操作会报错；因此，我们采用一个取巧方法，给 stack 赋初值 ? ，并在哈希表 dic 中建立 key:'?'，value:'? 的对应关系予以配合。
此时当 stack 为空且 c 为右括号时，可以正常提前返回 false；
字符串 s 以左括号结尾： 此情况下可以正常遍历完整个 s，但 stack 中遗留未出栈的左括号；因此，最后需返回 len(stack) == 1，以判断是否是有效的括号组合。

"""
