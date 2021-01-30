class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 == m:
            nums1[p1+p2:] = nums2[p2:]
        if p2 == n:
            nums1[p1+p2:] = nums1_copy[p1:]
"""
双指针法：
一般而言，对于有序数组可以通过 双指针法 达到O(n + m)的时间复杂度。
最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。
由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m) 的空间复杂度。
"""