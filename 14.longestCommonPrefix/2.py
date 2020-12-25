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

"""
排序的时候，先比较列表中所有元素的第一个字符的ASCll码值，再比较所有元素的第二个字符，一直到最后得出排序的结果。
所以在已经排序好的新列表中，各元素中如果从左到右有相同字符的话，一定是排在一起的，排序正是为了达到这个目的。

例子1：排序后，如果返回结果是'fl'，即strs[0]和strs[-1]有公共前缀'fl'，则说明中间所有元素前缀肯定都是'fl'（因为经过排序）。
例子2：排序后，如果返回结果是''，即strs[0]和strs[-1]没有公共前缀，那么既然有两个元素没有公共前缀，更不需要考虑中间元素了。

"""