def selectionSort(arr):
    for i in range(0, len(arr)-1): # 只循环到倒数第二位，最后直接对比倒数第二位和倒数第一位
        minIndex = i # 记录最小值的索引

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        # 如果不是最小值，则交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr
