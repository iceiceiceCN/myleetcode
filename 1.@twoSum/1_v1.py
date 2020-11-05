class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(0,lens):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
            else:continue
            if j >=0 and j != i:
                return [j,i]

if __name__ == "__main__":
    A = Solution()
    B = A.twoSum(nums=[2,5,5,11],target=10)
    print(B)
