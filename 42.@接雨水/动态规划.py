class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        max_right = [0] * n
        max_left = [0] * n
        max_left[0]  = height[0]
        max_right[n-1] = height[n-1]
        res = 0
        for i in range(1,n):
            if height[i] > max_left[i-1]:
                max_left[i] = height[i]
            else:
                max_left[i] = max_left[i-1]
            # 可以简化为：
            # max_left[i] = max(height[i],max_left[i-1])
        for i in range(n-2,-1,-1):
            if height[i] > max_right[i+1]:
                max_right[i] = height[i]
            else:
                max_right[i] = max_right[i+1]

        for i in range(n):
            if height[i] < min(max_right[i],max_left[i]):
                res += min(max_right[i],max_left[i]) - height[i]
        
        return res

m = [0,1,0,2,1,0,1,3,2,1,2,1]
a = Solution()
b = a.trap(m)

"""
我们发现在寻找每个下标的左边和右边最高的柱子时，会对柱子进行反复搜索导致复杂度降低，
假如我们使用两个数组 maxleft 和 maxright，
maxleft[i] 表示下标 i 左边最高柱子的高度,maxright[i] 表示下标 i 右边最高柱子的高度，
很明显，我们只需要一趟遍历就可以得到结果。这样由于避免了重复计算，时间复杂度会降低到 O(N)。
"""