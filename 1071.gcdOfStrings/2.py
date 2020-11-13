import math as m

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = m.gcd(len(str1), len(str2)) 
        # 既然是求最大公因子，那就先求出最大公约数，直接取最大公约数个数量的字符串进行对比
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''

"""
https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/solution/zi-fu-chuan-de-zui-da-gong-yin-zi-by-leetcode-solu/
"""