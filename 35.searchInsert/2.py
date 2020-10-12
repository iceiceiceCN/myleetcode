class Solution:
    def searchInsert(nums, target) :
        size = len(nums)

        if size == 0:
            return 0
        
        if target > nums[size-1]:
            return size

        left = 0
        right = size - 1

        while left < right: # 退出循环时,left 与 right 重合,[left, right]只剩下1个元素
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                return mid
        # 如果找到目标值则返回索引; 
        # 如果找不到目标值,left 为最接近目标值的,即插入位置.
        return left 

"""
二分搜索思路:
当题目中有隐含的单调性时,可以思考使用二分搜索.
    划分[left, mid]与[mid + 1, right],mid 被分到左边,对应 int mid = left + (right - left) / 2
    划分[left, mid - 1]与[mid, right],mid 被分到右边,对应 int mid = left + (right - left + 1) /2
"""

    