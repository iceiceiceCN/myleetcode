nums = [0,0,1,2,0,12]
# nums.remove(nums[0])
# print(nums)
# nums.append(0)
# print(nums)

count  = 0
i = 0
while i < len(nums):
    if nums[i] == 0:
        count += 1
        nums.remove(nums[i])
        i -= 1
    else: i += 1

while count > 0:
    nums.append(0)
    count -= 1

print(nums)
        
        


        # hash = {}
        # for i in range(len(nums)):
        #     hash[i] = nums[i]
        #     if nums[i] == 0:
        #         nums