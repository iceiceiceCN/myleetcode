def sift_down(arr, node, end):
    root = node
    # print(root,2*root+1,end)
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1  # left child
        if child > end:
            # print('break',)
            break
        print("v:", root, arr[root], child, arr[child])
        print(arr)

        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:  # 如果左边小于右边
            child += 1  # 设置右边为大
        
        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            tmp = arr[root]
            arr[root] = arr[child]
            arr[child] = tmp
            # 正在调整的节点设置为root
            #print("less1:", arr[root],arr[child],root,child)
            root = child
            #[3, 4, 7, 8, 9, 11, 13, 15, 16, 21, 22, 29]
            #print("less2:", arr[root],arr[child],root,child)
        else:
            # 无需调整的时候, 退出
            break
    # print(arr)
    print('-------------')


def heap_sort(arr):
    # 从最后一个有子节点的孩子还是调整最大堆
    first = len(arr) // 2 - 1
    for i in range(first, -1, -1):
        sift_down(arr, i, len(arr) - 1)
    #[29, 22, 16, 9, 15, 21, 3, 13, 8, 7, 4, 11]
    print('--------end---', arr)
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)
        # print(arr)

        
if __name__ == "__main__":
    print(heap_sort([5, 6, 8, 1, 2, 4, 9]))
