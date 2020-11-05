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
通过哈希来求解，这里通过字典来模拟哈希查询的过程。
这种办法其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。

nums = [2, 7, 11, 15] -> 
enumerate(nums) = [(0, 2), (1, 7), (2, 11), (3, 15)] (索引, 值)-> 
hashmap = {2: 0, 7: 1, 11: 2, 15: 3} {值: 索引}
通过hashmap.get(target - num)就能得到另一个加数的索引(数组下标)

执行用时：24 ms, 在所有 Python 提交中击败了85.44%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了8.88%的用户
"""

# print(twoSum(nums,target))