class Solution:
    def countBinarySubstrings(self, s):
        seq = [0, 1]
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq[1] += 1
            else:
                res.append(min(seq))
                seq[0] = seq[1]
                seq[1] = 1
        res.append(min(seq))
        return sum(res)
"""
对于一段"0" * a + "1" * b,或"1" * a + "0" * b而言，其所含的所有符合条件的子串个数为其中a与b中较小的值，
因此只需要不断的对这样的子串进行统计，并把结果加和即可
"""
if __name__ == "__main__":
    a = Solution()
    b = a.countBinarySubstrings("00110011")