class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = set(nums)
        for i in range(len(nums)+1):
            if i not in hash:
                return i 


"""
我们可以直接查询每个数是否在数组中出现过来找出缺失的数字。
如果使用哈希表，那么每一次查询操作都是常数时间的。

时间复杂度：O(n)。集合的插入操作的时间复杂度都是 O(1)，一共插入了 n 个数，时间复杂度为 O(n)。集合的查询操作的时间复杂度同样是 O(1)，最多查询 n+1 次，时间复杂度为 O(n)。因此总的时间复杂度为 O(n)。
空间复杂度：O(n)。集合中会存储 n 个数，因此空间复杂度为 O(n)

"""