class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_ = s.strip()
        return len(s_.split(' ')[-1])