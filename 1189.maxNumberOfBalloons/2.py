class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        text_count = Counter(text)  # Counter({'o': 4, 'l': 4, 'b': 2, 'a': 2, 'n': 2, 'g': 1, 'x': 1})
        balloon_dict = {
            'a': 1,
            'b': 1,
            'n': 1,
            'l': 2,
            'o': 2
        }
        result = []
        for key in balloon_dict.keys(): # 通过.keys()调用字典中的key
            if key in text_count:
                result.append(int(text_count[key]/balloon_dict[key]))
            else:
                return 0
        return min(result)

"""
气球的最大数量由最少的单子决定的，分别统计5个字母的个数，以及可以组成的balloon的个数，找出可以组成balloon最少的。
"""

if __name__ == "__main__":
    a = Solution()
    b = a.maxNumberOfBalloons("baoollnnololgbax")
    print(b)