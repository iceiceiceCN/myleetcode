class Solution:
    def twoSum(self,nums,target):
        lens = len(nums)
        j = -1
        for i in range(1,lens):
            temp = nums[:i] # 这里可以限定i != j
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                break
        if j >=0 :
            return [j,i]

if __name__ == "__main__":
    A = Solution()
    B  = A.twoSum(nums=[2,7,11,15],target=9)
    print(B)