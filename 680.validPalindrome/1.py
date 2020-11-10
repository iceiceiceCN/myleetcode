class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(x): return x == x[::-1]
        def startPart(s, x): return s[:x] + s[x+1:]
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(startPart(s, left)) or isPalindrome(startPart(s, right))
            right -= 1
            left += 1

        return True

"""
当左右两个指针遇到不等的元素时，按照题目最原本的意思，我们处理的方式是删除 左指针指向的字符 或者 右指针指向的字符，
判断 剩余的所有字符 是否可以构成回文串。
如果删除一个字符后，剩余的全部字符构成字符串 是回文字符串，那么就满足题意。
本方案的时间复杂度是：O(N)；由于我判断是否回文使用了 [::-1] 翻转形成了新字符串，所以空间复杂度是O(N)。
如果不通过翻转的方式来判断，空间复杂度可以降到O(1)。
"""

if __name__ == "__main__":
    a = Solution()
    b = a.validPalindrome("ebcbbececabbacecbbcbe")
