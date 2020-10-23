from collections import Counter

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left ,right, count = {},{},{}
        for idx,x in enumerate(nums):
            if x not in left: left[x] = idx
            right[x] = idx
            count[x] = count.get(x,0) + 1 # 计数 {1: 2, 2: 2, 3: 1}
        
        ans = len(nums)
        degree = max(count.values())

        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x]-left[x]+1)
        return ans