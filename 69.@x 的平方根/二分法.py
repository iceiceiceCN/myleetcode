class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # x (x ≠ 0) 的平方根一定是落在 [1, x/2 + 1] 区间，
        # 所以左右边界分别取 left = 1, right = x/2 + 1，而不分别取 0 和 x，这样可缩小查找范围。
        l, r = 1, x // 2 + 1

        while l <= r:
            m = (l + r) // 2

            sq = m * m
            if sq < x:
                l = m + 1 # 既然m不是，那直接取m+1, 下面同理
            elif sq > x:
                r = m - 1
            else:
                return int(m)
        return int(r)

a = Solution()
b = a.mySqrt(0)
print(b)

"""
至于 x (x ≠ 0) 的平方根一定是落在 [1, x/2 + 1] 区间，而不是落在 [1, x/2] 区间，
即右边界 right 取 x/2 + 1，而不取 x/2，这是因为当 x = 1 时，如果 right 取 x/2 的话，由于 x/2 = 0，
此时 left = 1，大于 right，以至于直接跳出循环，导致 x 的平方根为 0 。

"""