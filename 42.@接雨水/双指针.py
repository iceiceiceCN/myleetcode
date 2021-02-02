class Solution:
    def trap(self, height) :
        if not height:
            return 0
        n = len(height)
        left = 0
        right = n-1
        max_left = height[0]
        max_right = height[n-1]
        res = 0
        while left < right:
            max_left = max(height[left],max_left)
            max_right = max(height[right],max_right)

            # 较高的那一边不动 比较矮一点的那边开始收缩 防止[0,0,0,6]这种情况
            # 用矮的一方去遍历
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res
m = [4,2,0,3,2,5]
a = Solution()
b = a.trap(m)

"""
先找到左边与右边最高的地方，然后左右往里遍历，较矮的一方先动，因为右边有较高的一方，所以一定能装水。
然后较矮的一方遍历减去当前高度，就是当前单元装水的数量。

https://leetcode-cn.com/problems/trapping-rain-water/solution/dong-tai-gui-hua-shuang-zhi-zhen-tu-jie-by-ml-zimi/
"""