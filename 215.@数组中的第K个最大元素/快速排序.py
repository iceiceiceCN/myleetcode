def quick_sort(arr):
    if len(arr) < 2:
        # 基线条件：为空或只包含一个元素的数组是“有序”的
        return arr
    else:
        # 递归条件
        pivot = arr[0]
        print("pivot = " + str(pivot))

        # 由所有小于基准值的元素组成的子数组
        less = [i for i in arr[1:] if i <= pivot]

        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([3, 2, 4, 1, 59, 23, 13, 1, 3]))
