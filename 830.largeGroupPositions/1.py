class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        i = 0
        ans = []
        for j in xrange(len(s)):
            if j == len(s)-1 or s[j]!=s[j+1]: # 先判断j == len(s)-1 就不会出现指针越界的情况
                if j-i+1>=3:
                    ans.append([i,j])
                i = j+1
                """
                s="abbxxxxzzy"
                当j=2指到s[2]的时候，s[2]!=s[3]，这个时候i要跳到s[3]的位置开始记录
                """

        return ans