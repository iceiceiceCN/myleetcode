class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                return [i, nums[i+1:].index(tmp)+(i+1)]


if __name__ == "__main__":
    A = Solution()
    B = A.twoSum(nums=[3, 2, 4], target=6)
    print(B)
