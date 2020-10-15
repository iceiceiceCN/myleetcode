class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)
        
        elif nums[0] != 0:
            return 0
        
        else:
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1] + 1 :
                    return nums[i-1] + 1


"""
排序方法:
首先我们对数组进行排序，随后我们可以在常数时间内判断两种特殊情况：
0 没有出现在数组的首位，以及 nn 没有出现在数组的末位。
如果这两种特殊情况都不满足，那么缺失的数字一定在 0 和 nn 之间（不包括两者）。
此时我们可以在线性时间内扫描这个数组，如果某一个数比它前面的那个数大了超过 1，那么这两个数之间的那个数即为缺失的数字。

时间复杂度：O(nlogn)。由于排序的时间复杂度为 O(nlogn)，扫描数组的时间复杂度为 O(n)，因此总的时间复杂度为O(nlogn)。
空间复杂度：O(1) 或 O(n)。空间复杂度取决于使用的排序算法，根据排序算法是否进行原地排序（即不使用额外的数组进行临时存储），空间复杂度为 O(1)O(1) 或 O(n)O(n)。
"""