class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        vote = 0

        for i in nums:
            if vote == 0:
                major = i
            if i == major:
                vote += 1
            else:
                vote -= 1
        
        return major

"""
摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」，
算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。

算法可以分为两个阶段：
1.对抗阶段：分属两个候选人的票数进行两两对抗抵消
2.计数阶段：计算对抗结果中最后留下的候选人票数是否有效

根据上述的算法思想，我们遍历投票数组，将当前票数最多的候选人与其获得的（抵消后）票数分别存储在 major 与 count 中。

当我们遍历下一个选票时，判断当前 count 是否为零：
若 count == 0，代表当前 major 空缺，直接将当前候选人赋值给 major，并令 count++
若 count != 0，代表当前 major 的票数未被完全抵消，因此令 count--，即使用当前候选人的票数抵消 major 的票数

"""