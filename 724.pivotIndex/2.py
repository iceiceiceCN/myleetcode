class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        left_sum = 0
        for i,num in enumerate(nums):
            if left_sum == S - num - left_sum:
                return i
            left_sum += num
        return -1

"""
不要用sum去算，直接累加算是最快的
用sum的话需要1000+ms
不用sum则需要40ms
"""