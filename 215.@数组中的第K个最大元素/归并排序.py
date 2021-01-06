def mergeSort(arr):
    import math
    if(len(arr) < 2):
        return arr
    middle = len(arr)//2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


print(mergeSort([3, 2, 4, 1, 59, 23, 13, 1, 3]))

"""
归并排序是分治法的典型应用。分治法（Divide-and-Conquer）：将原问题划分成 n 个规模较小而结构与原问题相似的子问题；
递归地解决这些问题，然后再合并其结果，就得到原问题的解，分解后的数列很像一个二叉树。

具体实现步骤：
1.使用递归将源数列使用二分法分成多个子列
2.申请空间将两个子列排序合并然后返回
3.将所有子列一步一步合并最后完成排序
4.注：先分解再归并

"""