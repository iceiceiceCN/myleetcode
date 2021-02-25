class Solution:
    def twoSum(self,nums,target):
        lens = len(nums)
        j = -1
        for i in range(1,lens):
            temp = nums[:i] 
            # 这里可以限定i != j ; 如果用nums[i:]去找索引的话，
            # 新数组的索引是从0开始算的，要在新索引前面 +(i+1)，参考下方注释代码
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                break

        return [j,i]

if __name__ == "__main__":
    A = Solution()
    B  = A.twoSum(nums=[2,7,11,15],target=9)
    print(B)

"""
num2 的查找并不需要每次从 nums 查找一遍，只需要从 num1 位置之前或之后查找即可。
但为了方便 index 这里选择从 num1 位置之前查找。

较少的数组能更快的搜索，如果一直搜索不到的话，数组会慢慢变大。

执行用时：284 ms, 在所有 Python 提交中击败了60.19%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了21.48%的用户



class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                return [i, nums[i+1:].index(tmp)+(i+1)]
"""