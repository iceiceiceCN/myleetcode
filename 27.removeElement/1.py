class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        lens = 0
        times = 0
        raw_lens = len(nums)
        while times < raw_lens:
            times += 1
            if nums[j] == val :
                nums.remove(nums[j])
                lens += 1
            else:
                j += 1

        return raw_lens - lens