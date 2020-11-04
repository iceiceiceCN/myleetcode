class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:return False
        return True

# 检查ransomNote的每个字符是否在magazine字符串中:
# 如果在则在maazine中移除该一个字符串；
# 如果不在，则无法构成，返回False
# 时间复杂度: O(N^2) - N（遍历ransomNote） * N（replace最糟糕的情况是遍历整个magazine）
# 空间复杂度: O(1)