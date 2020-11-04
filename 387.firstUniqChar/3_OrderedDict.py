from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        odcit = OrderedDict()

        for i, val in enumerate(s):
            if val in odcit:
                odcit[val] += 1
            else:
                odcit[val] = 1

        for k, v in odcit.items(): # 必须要使用odcit.items() 才能得到有序字典，不能用enumerate(odict),使用后者的话得到的字典还是无序的。
            if v == 1:
                return s.index(k)

        return -1

if __name__ == "__main__":
    A = Solution()
    B = A.firstUniqChar("leetcode")