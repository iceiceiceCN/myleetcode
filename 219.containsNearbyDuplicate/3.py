class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:return False
        dct = dict()
        for inx,i in enumerate(nums):
            if i not in dct:
                dct[i] = inx
            else:
                if inx-dct[i] <= k:
                    return True
                else:
                    dct[i] = inx
        
        return False