class Solution:
    def matrixReshape(self, nums, r, c):
        m,n = len(nums),len(nums[0])

        if m*n != r*c:
            return nums
        
        res = [i for j in nums for i in j]
        # 先从nums中取出j，然后再从j中取出i，然后把i放在res里
        # 得到[1,2,3,4]
        print(res)

        new = [res[i:i+c] for i in range(0,len(res),c)]
        # 由于c是列数，所以每c个元素为一行
        # 得到[[1,2,3,4]]

        return new

if __name__ == "__main__":
    nums = [[1,2],[3,4]]
    r = 1
    c = 4
    A = Solution()
    B = A.matrixReshape(nums,r,c)