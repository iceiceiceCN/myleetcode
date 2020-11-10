class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=Counter(moves)
        return c['U']==c['D'] and c['L']==c['R']
# 先通过Counter遍历一次moves统计所有方向的数量，然后对比数量可获得结果，时间复杂度是O(N)，
# 而且算法时间复杂度的常数相较于2.py会小一些。