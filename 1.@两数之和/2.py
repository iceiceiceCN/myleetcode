class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(0,lens):
            if target - nums[i] in nums: # 先判断是否有该值，如果存在该值则返回索引
                j = nums.index(target - nums[i])
            else:continue # 如果没找到就赶紧进行下一轮，不能继续往下执行，否则会输出错误答案
            if j != i: # 该值存在且不为自身
                return [i,j] # 可以按任意顺序返回答案

if __name__ == "__main__":
    A = Solution()
    B = A.twoSum(nums=[2,5,5,11],target=10)
    print(B)

"""
先判断是否有该值，然后再返回索引值，最后判断是否合法再返回

执行用时：452 ms, 在所有 Python 提交中击败了56.18%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了21.72%的用户
"""