class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        s_hash = {}
        for i, val in enumerate(s):
            if val in s_hash:
                s_hash[val] += 1
            else:
                s_hash[val] = 1
        for i,val in enumerate(s):
            if s_hash[val] == 1:
                return i

        return -1

"""
哈希表方法，遍历s记录出现次数，然后再次遍历s，找到最先出现的哈希值为1的字符
"""