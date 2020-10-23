from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        res = c.most_common(1)[0][0]

        return res
        # return c

# nums = [3,2,3,1,2,2,2]

# if __name__ == "__main__":
#     A = Solution()
#     B = A.majorityElement(nums)
#     print(B.most_common(1)[0][0])
#     print(B.most_common(1)) # [(2, 4)] 输出为key 和 frequency



"""
哈希表方法

1. 统计“可迭代序列”中每个元素的出现的次数
#对列表作用
list_01 = [1,9,9,5,0,8,0,9]  #GNZ48-陈珂生日
print(Counter(list_01))  #Counter({9: 3, 0: 2, 1: 1, 5: 1, 8: 1})

#对字符串作用
temp = Counter('abcdeabcdabcaba')
print(temp)  #Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
#以上其实是两种使用方法，一种是直接用，一种是实例化以后使用,如果要频繁调用的话，显然后一种更简洁


print(temp.items()) #dict_items([('e', 1), ('c', 3), ('b', 4), ('d', 2), ('a', 5)])
for item in temp.items():
    print(item)
('a', 5)
('c', 3)
('d', 2)
('e', 1)
('b', 4)
--------------------------------------------------------------
2. 利用most_common()方法求序列中出现次数最多的元素

list_01 = [1,9,9,5,0,8,0,9]
temp = Counter(list_01)

#统计出现次数最多的一个元素
print(temp.most_common(1))   #[(9, 3)]  元素“9”出现3次。
print(temp.most_common(2)) #[(9, 3), (0, 2)]  统计出现次数最多个两个元素

#没有指定个数，就列出全部
print(temp.most_common())  #[(9, 3), (0, 2), (1, 1), (5, 1), (8, 1)]

--------------------------------------------------------------
3. elements()和sort()方法

c = Counter('ABCABCCC')
print(c.elements()) #<itertools.chain object at 0x0000027D94126860>

#尝试转换为list
print(list(c.elements())) #['A', 'A', 'C', 'C', 'C', 'C', 'B', 'B']

#或者这种方式
print(sorted(c.elements()))  #['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C']

#这里与sorted的作用是： list all unique elements，列出所有唯一元素
#例如
print( sorted(c) ) #['A', 'B', 'C']

-------------------------------------------------------------
4. 计算元素总数/Keys()&Values()

c = Counter('ABCABCCC')
print(sum(c.values()))  # 8  total of all counts

print(c.keys())  #dict_keys(['A', 'B', 'C'])
print(c.values())  #dict_values([2, 2, 4])

------------------------------------------------------------
5. 对具体元素的操作

c = Counter('ABBCC')
#查询具体某个元素的个数
print(c["A"])  #1
------------------------------------------------------------
6. “与”和“或”操作

print(Counter('AAB') & Counter('BBCC'))
#Counter({'B': 1})

print(Counter('AAB') | Counter('BBCC'))
#Counter({'A': 2, 'C': 2, 'B': 2})
"""