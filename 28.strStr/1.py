class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle) # 或者haystack.find(needle)
        else:
            return -1

if __name__ == "__main__":
    A  = Solution()
    B  = A.strStr(haystack = "aaaaa", needle = "")
    print(B)