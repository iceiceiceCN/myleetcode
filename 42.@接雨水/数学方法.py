class Solution:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        res_left = 0
        res_right = 0
        max_left = 0
        max_right = 0

        for i in range(n):
            if height[i] > max_left:
                max_left = height[i]
            res_left += max_left

            if height[n-1-i] > max_right:
                max_right = height[n-1-i]
            res_right += max_right

        res = (res_left + res_right) - max_left * n - sum(height)
        return res

# https://leetcode-cn.com/problems/trapping-rain-water/solution/wei-en-tu-jie-fa-zui-jian-dan-yi-dong-10xing-jie-j/
"""
积水面积 = S1 + S2 - 矩形面积 - 柱子面积
"""