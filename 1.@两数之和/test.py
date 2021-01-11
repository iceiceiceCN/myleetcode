class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        j = -1
        for i in range(n):
            temp = nums[:i]
            t = target - nums[i]
            if t in temp:
                j = temp.index(t)
                break

            return [i, j]


if __name__ == "__main__":
    A = Solution()
    B = A.twoSum(nums=[2, 7, 11, 15], target=6)
    print(B)
