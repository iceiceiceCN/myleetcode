class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float("-inf") # 设置为负无穷
        for num in nums:
            if num >third:
                if num < second: # 更新第三大的数
                    third = num
                elif num > second:
                    if num < first: # 两个数要往后面推
                        third = second
                        second = num
                    elif num > first: # 三个数要往后面推
                        third = second
                        second = first
                        first = num
        if third == float("-inf"): # 判断[1,1,1,1]这种情况
            return first
        else:
            return third