class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = True
        max_len = 1
        start = 0
        for j in range(1,size):
            for i in range(0,j):
                if s[i] == s[j]:
                    if j - i <3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1] 
                else:
                    dp[i][j] = False
            
                if dp[i][j]:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        start = i
                        max_len = cur_len
        
        return s[start:start+max_len]

a = Solution()
b = a.longestPalindrome("babad")

# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/