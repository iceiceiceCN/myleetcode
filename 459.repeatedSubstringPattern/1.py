class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s+s)[1:-1]
        # 如果s中包含重复的子字符串，那么说明s中至少包含两个子字符串，s+s至少包含4个字串，前后各去掉一位，
        # 查找s是否在新构建的字符串中。