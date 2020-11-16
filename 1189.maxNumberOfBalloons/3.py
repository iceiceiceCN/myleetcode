class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        o = text.count("o")
        l = text.count("l")
    
        return int(min(o//2 , l//2 , text.count("b") , text.count("a") , text.count("n")))

"""
找到判断字符串的关键，那就是数量需要对得上
"""