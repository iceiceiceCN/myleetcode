class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k]) # 先取得前k之和
        res = s
        for i in range(k,len(nums)): # 滑动窗口遍历k之和，找到最大k之和
            s += nums[i] - nums[i-k]
            res = max(res,s)

        return res/k

if __name__ == "__main__":
    nums =[1,12,-5,-6,50,3]
    k = 4
    A = Solution()
    B = A.findMaxAverage(nums,k)
    print(B)