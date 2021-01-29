class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2+1  # 在边界值加一
        while left < right:
            mid = left + (right-left)//2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                right = mid
            else:
                left = mid + 1

        return left


"""
每一轮区间被划分成 2 部分，理解 区间划分 决定中间数取法（ 无需记忆，需要练习 + 理解 ），在调试的过程中理解 区间和中间数划分的配对关系：
***
划分 [left, mid] 与 [mid + 1, right] ，mid 被分到左边，对应 (left + right) / 2
划分 [left, mid - 1] 与 [mid, right] ，mid 被分到右边，对应 (left + right + 1) / 2

https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
二分法模板
"""
