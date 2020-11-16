class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        left = 0
        right = -1
        num = 0
        for k, v in enumerate(s):
            if v == 'R':
                count += 1
            elif v == 'L':
                count -= 1
            
            if count == 0:
                num += 1
        
        return num
            