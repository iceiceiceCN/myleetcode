class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_new = s[::-1]
        s_new = s_new.split()[::-1]
        s_new = " ".join(s_new)
        return s_new

# 在python中，字符串是不可变对象，不能通过下标的方式直接赋值修改。
# 不可变对象有：数字、字符串和元组。


if __name__ == "__main__":
    a = Solution()
    b = a.reverseWords(s="Let's take LeetCode contest")
    print(b)