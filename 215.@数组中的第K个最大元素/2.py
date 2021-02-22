class Solution:
    def findKthLargest(self, nums, k):
        def quick_sort(mynums):
            if len(mynums)<2: # 如果数组只有 1 位数字了，那就不用sort了
                return mynums
            else:
                p = mynums[0]

                small = [num for num in mynums[1:] if num < p] # 每次都拿数组中第一位的数字与数组中所有字符挨个对比，比 p 小的进入 small 数组
                big = [num for num in mynums[1:] if num >= p] # 每次都拿数组中第一位的数字与数组中所有字符挨个对比，比 p 小的进入 big 数组

            # 然后再对 small 和 big 数组进行 quick_sort(),使这两个数组也都有序
            return quick_sort(small) + [p] + quick_sort(big)

        res = quick_sort(nums)

        return res[-k] 

if __name__ == "__main__":
    a = Solution()
    b = a.findKthLargest([5, 6, 8, 1, 2, 4, 9],3)