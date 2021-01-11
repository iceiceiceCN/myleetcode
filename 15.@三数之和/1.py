class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()  # 首先进行排序，方便后面使用指针

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # 相同的num直接跳过，因为属于冗余计算。i=0的时候，i-1会溢出
                continue
            l = i+1
            r = n-1
            while l < r:
                temp = nums[i]+nums[l]+nums[r]  # 得到当前三数相加结果 用于后面进行比较
                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]])  # 包装结果
                    l += 1
                    r -= 1
                    # 只要没有左右指针碰撞，就继续缩小范围，跳过冗余计算
                    while l < r and nums[l] == nums[l-1]: # 一定是和刚刚计算过的比较，而不是和下一个要计算的比较
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif temp > 0:  # 大于0说明右边的数大了，应该往左移
                    r -= 1
                else:  # 小于0说明左边的数小了，应该往右移
                    l += 1
        return res

"""
基本思想和两数之和一样
相当于固定一个数，然后继续两数之和
"""