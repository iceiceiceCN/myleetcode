class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        left,right = 0,len(nums)-1

        while left <= right: # 一定是*小于等于*
            mid = (left + right) //2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # 必须要带等于号，因为[3,1]时，left = mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                
            elif nums[mid] <= nums[right]: # 同理
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
    
        return -1

"""
任何时候都有一边是有序数组
先找出左右哪一边是有序数组，然后通过将target与有序数组的最大值和最小值对比，
来判断target属于左边数组还是右边数组
"""

a = Solution()
n = [3,1]
t = 0
b = a.search(n,t)
print(b)