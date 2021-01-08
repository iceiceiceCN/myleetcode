class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(mynums):
            if len(mynums)<2:
                return mynums
            else:
                p = mynums[0]

                small = [num for num in mynums[1:] if num < p]
                big = [num for num in mynums[1:] if num >= p]

            return quick_sort(small) + [p] + quick_sort(big)

        res = quick_sort(nums)

        return res[-k] 