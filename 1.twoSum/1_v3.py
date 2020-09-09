# nums = [2, 7, 11, 15]
# target = 9

# print(list(enumerate(nums)))

# hashmap={}
# for ind,num in enumerate(nums):
#     hashmap[num] = ind

# print(hashmap)

def twoSum(nums,target):
    hashmap = {}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]

# print(twoSum(nums,target))