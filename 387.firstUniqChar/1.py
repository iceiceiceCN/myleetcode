class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:return -1
        s_hash = {}
        for i,val in enumerate(s):
            if val in s_hash:
                s_hash[val] = len(s)
            else:
                s_hash[val] = i
        
        return -1 if min(s_hash.values()) == len(s) else min(s_hash.values())

"""
哈希表方法，遍历s记录索引，然后返回哈希值最小的值，此处的哈希值即是索引
"""