class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        windows=set() # 不会重复的{}
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            windows.add(nums[i])
            if len(windows)>k:
                windows.remove(nums[i-k])  # 维护一个k大小的窗口，如果超过了k，则删除最旧的元素，因为已经超过k的距离，就算相同也没用
        return False
"""
用散列表来维护这个k大小的滑动窗口
遍历数组，对于每个元素做以下操作：
    在散列表中搜索当前元素，如果找到了就返回 true。
    在散列表中插入当前元素。
    如果当前散列表的大小超过了 k， 删除散列表中最旧的元素。

"""
if __name__ == "__main__":
    A = Solution
    B = A.containsNearbyDuplicate(nums=[1,0,1,1],k=1)
    print(B)