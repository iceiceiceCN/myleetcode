def bubbleSort(arr):
    compare_count = 0
    length = len(arr)
    for i in range(length-1):
        for j in range(length-i-1):  # 每次排序都会把最大的数排到最后一位
            compare_count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('compare_count = '+str(compare_count)) # 10
    return arr


def bubbleSort2(arr):
    """
    如果没有元素交换，说明数据在排序过程中已经有序，直接退出循环
    """
    compare_count = 0
    length = len(arr)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            compare_count += 1
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break               # Stop iteration if the collection is sorted.
    print('compare_count = '+str(compare_count)) # 7
    return arr


def bubbleSort3(arr):
    """
    bubble_sort2的基础上再优化。
    优化思路：在排序的过程中，数据可以从中间分为两段，一段是无序状态，另一段是有序状态。（冒泡排序时，某些数据的后半部分本来已经接近有序，可以省略）
    每一次循环的过程中，记录最后一个交换元素的位置，它便是有序和无序状态的边界
    下一次仅循环到边界即可，从而减少循环次数，达到优化。
    """
    length = len(arr)
    last_index = -1
    compare_count = 0
    border = length - 1
    for i in range(length-1):
        swapped = False
        for j in range(border):
            compare_count += 1
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
                last_index = j
        if not swapped:
            break
        border = last_index     # 最后一个交换的位置就是边界
    print('compare_count = '+str(compare_count)) # 7
    return arr        


if __name__ == "__main__":
    t = [3,4,2,1,5,6,7,8]
    res = bubbleSort3(t)
    print(res)
