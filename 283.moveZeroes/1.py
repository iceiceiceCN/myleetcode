class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        start = 0
        for i in nums: # 不要用range(len(nums)),使用索引会很麻烦，因为要删去元素，下标不好控制，直接从nums里抽值就行
            if i == 0 and start < zero_count:
                nums.remove(i)
                nums.append(0)
                start += 1
        return nums
