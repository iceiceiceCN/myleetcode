class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        end = len(s)-1
        while end >= 0 and s[end] == ' ':
            end -= 1
        
        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1
        
        return end-start


if __name__ == "__main__":
    A = Solution()
    B = A.lengthOfLastWord(" my life ")
"""
从后面开始找，先找到最后一个单词的最后一个字母下标为end
再从end开始找，找到最后一个单词的第一个字母的前一位下标start
最终end - start即为长度
"""