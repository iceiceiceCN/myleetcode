class Solution(object):
    def findDisappearedNumbers(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1 # 因为元素在过程中可能会被设置为负数
            if nums[new_index] > 0 :
                nums[new_index] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                res.append(i+1)
        return res


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    A = Solution()
    B = A.findDisappearedNumbers(nums)
    print(B)


"""
将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
举个例子：
原始数组：[4,3,2,7,8,2,3,1]
重置后为：[-4,-3,-2,-7,8,2,-3,-1]
结论：[8,2] 分别对应的index为[5,6]（消失的数字）

------------------------------------------------------------------------------------

若将题目要求改为数组中每个元素出现的可能次数是 n 次,求出数组中出现此次为偶数（奇数）次的元素（出现 0 次也算偶数次）。

class Solution(object):
    def findDisappearedNumbers(self, nums):
        # 将所有正数作为数组下标，置对应数组值为相反数。那么，仍为正数的位置即为出现偶数次(未出现是0次，也是偶数次)数字。
        # 举个例子：
        # 原始数组：[1, 1, 1, 1, 2, 3, 4, 5]
        # 重置后为：[1, -1, -1, -1, -2, 3, 4, 5]
        # 结论：[1,3,5,6] 分别对应的index为[1,6,7,8]（消失的数字）
        for num in nums:
            index = abs(num) - 1
            # 保持nums[index]为相反数,唯一和上面的解法不同点就是这里，好好体会
            nums[index] = -nums[index]
        #偶数次
        return [i + 1 for i, num in enumerate(nums) if num > 0] # 偶数次求负 结果为正
        #奇数次
        return [i + 1 for i, num in enumerate(nums) if num < 0] # 奇数次求负 结果为负

"""


