class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs): # tmp = ('a', 'a', 'a')
            tmp_set = set(tmp) # tmp_set = {'a'}
            if len(tmp_set) == 1:
                res += tmp[0] # res = 'a'
            else:
                break
        return res


if __name__ == "__main__":
    A = Solution()
    B = A.longestCommonPrefix(["abc","ab","ab"]) # 输出的是ab 解压的时候多出来的c会省去


"""
A = ["flower","flow","flight"]

list(zip(*A)) 
# [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
"""