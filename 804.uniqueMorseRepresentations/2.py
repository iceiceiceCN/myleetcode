class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        res = set() # 去重集合
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            s= '' # 每次加完需要重新清空字符串s
            for i in word:
                s += morse[ord(i)-ord('a')]
            res.add(s)
        
        return len(res)
        
if __name__ == "__main__":
    a = Solution()
    b,M = a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(b)
    print(M)