class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if temp + nums[j] == target:
                    res = [i,j]
                    return res

"""
遍历匹配法：
两层for循环。在第一个for循环中取一个数，然后再第二个for循环中遍历判断temp + nums[j] == target

时间复杂度：O(N^2)
执行用时：4800 ms, 在所有 Python3 提交中击败了28.72%的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了65.82%的用户
"""