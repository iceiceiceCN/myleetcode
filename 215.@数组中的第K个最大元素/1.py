class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums,reverse=True)
        return res[k-1]


"""
.sort()方法
使用方式是：列表.sort(),作用是将原来的列表正序排序，所以它是对原来的列表进行的操作，不会产生一个新列表
numList.sort()执行过程是将列表拍完序后又赋值给了原列表
无法将numList.sort()赋值给一个新列表，因为它并不返回一个新列表


sorted(列表),是Python内置函数，该函数对原列表不会产生影响，只是在原来列表的基础上，产生一个有序的新列表，可以复制一个列表名
sorted排序后的数组，不会对原列表有任何影响
"""
