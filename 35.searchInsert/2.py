def searchInsert(nums, target) :
    size = len(nums)

    if size == 0:
        return 0
    
    if target > nums[size-1]:
        return size

    left = 0
    right = size - 1

    while left < right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            return mid

    return left



    