nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    tmp = nums[0]  # tmp记录当前和
    max_ = tmp  # max_记录最大和
    n = len(nums)
    for i in range(1, n): 
        if tmp + nums[i] > nums[i]: #当前序列 + 下一个元素 能组成更大的序列，说明最大序列可能出现
            tmp = tmp + nums[i] # 更新当前序列和
            max_ = max(tmp, max_) # 记录当前的最大序列和
        else:   #当前序列 + 下一个元素 不能组成更大的序列 则重新开始寻找序列
            max_ = max(tmp, nums[i], max_) # 记录当前的最大序列和
            tmp = nums[i] # 从当前位置重新开始寻找
    return max_

maxSubArray(nums)