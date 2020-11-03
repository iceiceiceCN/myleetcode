class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def calShiftMat(st):
            dict = {}
            for i in range(len(st)-1,-1,-1):
                if st[i] not in dict:
                    dict[st[i]] = len(st) - i
            dict["ot"] = len(st) + 1
            return dict

        if len(needle) > len(haystack):return -1
        elif needle is None: return 0

        dic = calShiftMat(needle)
        idx = 0
        while idx + len(needle) <= len(haystack):
            str_cut = haystack[idx:idx+len(needle)] # haystack[idx:idx+len(needle)] 取到的是下标为 idx+len(needle)-1的位置，没有越界
            if str_cut == needle:
                return idx
            else:
                if idx + len(needle) == len(haystack):return -1 # 也可以写成 >=
                tmp = haystack[idx+len(needle)] # 但是这里是实打实的取到了idx+len(needle)的位置，是越界情况
                if dic.get(tmp):
                    idx = dic[tmp] + idx
                else:
                    idx = dic["ot"] + idx
        
        return -1 if idx + len(needle) >= len(haystack) else idx


"""
Sunday算法:
匹配机制
-目标字符串 haystack
-模式串 needle
-当前查询索引 idx (初始为0)
-待匹配字符串 str_cut: haystack[idx:idx+len(needle)]

每次匹配都会从 目标字符串中 提取 待匹配字符串 与 模式串 进行匹配：
-若匹配，则返回当前 idx
-不匹配，则查看 待匹配字符串 的*后一位字符* c：
    1.若 c 存在于needle中，则idx = idx + 偏移表[c]
    2.否则，idx = idx + len(needle)
repeat loop直到idx + len(needle) > len(haystack)


偏移表的作用是存储每一个在 模式串 中出现的字符，在 模式串 中出现的最右位置到尾部的距离 +1，例如 aab：
-a 的偏移位就是 len(pattern)-1 = 2
-b 的偏移位就是 len(pattern)-2 = 1
-其他的均为 len(pattern)+1 = 4
"""

if __name__ == "__main__":
    A  = Solution()
    B  = A.strStr(haystack = "aaaaa", needle ="bba")
    print(B)