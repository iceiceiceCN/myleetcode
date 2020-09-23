class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = [i * 10**index for index,i in enumerate(digits[::-1])]
        nums = sum(a) + 1
        return [int(x) for x in str(num)]
"""
把list转为int 然后加一，再int转为str然后再转为list
"""