class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Gauss_sum = (len(nums) * (len(nums)+1)) // 2
        actual_sum = sum(nums)
        return Gauss_sum - actual_sum

"""
我们可以用 高斯求和公式 求出 [0..n] 的和，减去数组中所有数的和，就得到了缺失的数字。

时间复杂度：O(n)。求出数组中所有数的和的时间复杂度为 O(n)，高斯求和公式的时间复杂度为 O(1)，因此总的时间复杂度为 O(n)。
空间复杂度：O(1)。算法中只用到了 O(1) 的额外空间，用来存储答案。
"""