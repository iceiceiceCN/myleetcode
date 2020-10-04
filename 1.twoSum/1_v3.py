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
"""
nums = [2, 7, 11, 15] -> 
enumerate(nums) = [(0, 2), (1, 7), (2, 11), (3, 15)] -> 
hashmap = {2: 0, 7: 1, 11: 2, 15: 3}
通过hashmap.get(target - num)就能得到另一个加数的索引(数组下标)
"""

# print(twoSum(nums,target))