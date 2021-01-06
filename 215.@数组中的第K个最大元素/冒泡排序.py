def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i): # 每次排序都会把最大的数排到最后一位
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == "__main__":
    t = [9,1,3,4,5]
    res = bubbleSort(t)
    print(res)