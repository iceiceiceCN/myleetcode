from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        par = paragraph.lower().split()

        res = Counter(par)
        max = -1
        flag = -1
        for k, v in res.items():  # 使用Counter的时候要用 k,v .items()
            if v > max and k not in banned:
                max = v
                flag = k

        return flag


if __name__ == "__main__":
    a = Solution()
    b = a.mostCommonWord(
        paragraph="Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"])
