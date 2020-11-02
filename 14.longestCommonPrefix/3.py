class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        res = strs[0]
        i = 1
        while i <len(strs): # 逐个对比
            while strs[i].find(res) != 0: 
            # 如果没找到就返回-1；如果找到了就返回找到的起始索引，由于是公共前缀，所以如果找到一定是从0索引开始
                res = res[0:len(res)-1]
            i += 1
        return res

"""
执行用时：12 ms, 在所有 Python 提交中击败了98.49%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.62%的用户
"""