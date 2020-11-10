class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(x): return x == x[::-1]
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
            right -= 1
            left += 1

        return True
"""
我们注意到1.py中，在找到第一个不相等的元素后，删除了不相等的一个元素，判断 剩余的所有字符 是不是回文字符串。
这个做法和题目最原本的意思完全一致。是否可以简化呢？
分析发现，在找到不相等的元素时，[0, left) 和 (right, len(s) - 1] 这两部分已经判断过是回文的，因此不用再次判断。
只用判断 [left, right] 区间中的字符串，即删除 left 或者 right 指向的元素，剩余的区间 (left, right] 或者 [left, right) 是否为回文串。
若 (left, right] 或者 [left, right) 为回文串，则说明删除了一个字符可以构成回文串。

如题目的示例 2 ，当左右指针遇到了不等元素时，删除 left 或者 right 指向元素后， 我们只用判断 c 或者 b 是否为回文串。
由于这两者是回文串，所以总体的字符串 s 删除 left 或者 right 指向元素也可以构成回文串。

本方案的时间复杂度是：O(N)；由于我判断是否回文使用了 [::-1] 翻转形成了新字符串，所以空间复杂度是O(N)。
如果不通过翻转的方式来判断，空间复杂度可以降到O(1)。
这个方案在找到左右指针不等的字符后，所要检查的字符串更少。
"""
if __name__ == "__main__":
    a = Solution()
    b = a.validPalindrome("ebcbbececabbacecbbcbe")
