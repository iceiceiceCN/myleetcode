class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''

        strs.sort() # 经过sort()之后，只比较strs[0]和strs[-1] 就能确定公共前缀
        start = strs[0]
        end = strs[-1]
        flag = -1
        for i,val in enumerate(start):
            if start[i] == end[i]:
                flag = i
                continue
            else:
                break
        
        return start[:flag+1] # [:1]得到是index=0，[:2]得到index=0,1


if __name__ == "__main__":
    A = Solution()
    B = A.longestCommonPrefix(["flower","flow","flight"]) 