class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]


nums = [3,2,3]



if __name__ == "__main__":
    A = Solution()
    B = A.majorityElement(nums)
    print(B)


"""
题目说了出现次数最多的数一定超过长度的一半，排序之后取中间的数，
如果满足题意则该数一定是出现次数最多的
"""