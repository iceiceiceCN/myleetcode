class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hash = {'a':0,'b':0,'l':0,'o':0,'n':2}
        count = 0
        for idx, val in enumerate(text):
            if val in "balon":
                hash[val] += 1
                
        hash['l'] //=2
        hash['o'] //=2
        return min(hash['a'],hash['b'],hash['l'],hash['o'],hash['n'])


if __name__ == "__main__":
    a = Solution()
    b = a.maxNumberOfBalloons("baoollnnololgbax")
    print(b)
