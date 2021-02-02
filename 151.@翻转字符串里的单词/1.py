class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.strip().split() # 先strip() 再split()
        strs = t[::-1]
        return ' '.join(strs)