class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        M = {"".join(Morse[ord(c) - ord('a')] for c in word) for word in words}
        
        return len(M),M

"""
我们将数组 word 中的每个单词转换为摩尔斯码，并加入哈希集合（HashSet）中，
最终的答案即为哈希集合中元素的个数。 (HashSet自动去重)
"""
if __name__ == "__main__":
    a = Solution()
    b,M = a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(b)
    print(M)