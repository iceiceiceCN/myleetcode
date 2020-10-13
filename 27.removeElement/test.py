# def searchInsert(nums, target) :
#     size = len(nums)

#     if size == 0:
#         return 0
    
#     if target > nums[size-1]:
#         return size

#     left = 0
#     right = size - 1

#     while left < right:
#         mid = (left + right)//2
#         if nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid
#         elif nums[mid] == target:
#             return mid

#     return left


# nums = [1,3,5,6]
# target = 1
# print(searchInsert(nums,target))

# read_stop_pos = 101
# window_stop_id = int(read_stop_pos / 50) + 1 if read_stop_pos % 50 else int(read_stop_pos / 50)
# print(window_stop_id)

# a=0
# if a :
#     print("yes")
# else:
#     print("No")


# a = str('M')
# s = eval(a) * 10
# print(s)