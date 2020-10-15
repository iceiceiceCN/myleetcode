class Solution(object):
    def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash = {}
        for i in range(len(nums)):
            if (nums[i] not in hash):
                hash[nums[i]] = i
            else:
                if i - hash[nums[i]] <= k:
                    return True
                else:
                    hash[nums[i]] = i # 更新位置 寻找下一个
        return False

if __name__ == "__main__":
    A = Solution
    B = A.containsNearbyDuplicate(nums=[1,0,1,1],k=1)
    print(B)