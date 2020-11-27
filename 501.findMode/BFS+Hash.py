# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        # 用字典存每个节点出现的值
        dicts = {}

        # 使用BFS访问每个节点的值
        deque = collections.deque()
        deque.append(root)

        while len(deque) > 0:
            currVal = deque.popleft()
            if currVal.val not in dicts:
                dicts[currVal.val] = 1
            else:
                dicts[currVal.val] += 1

            if currVal.left:
                deque.append(currVal.left)
            if currVal.right:
                deque.append(currVal.right)

        # print(dicts,max(dicts.values()))
        maxVal = max(dicts.values())
        res = []
        for item, val in dicts.items():
            if val >= maxVal:
                res.append(item)
        return res
"""
hash字典操作：

获取字典中最大/最小值对应的键:
1：利用min(dict, key=dict.get)或者max(dict, key=dict.get)
d = {1:1, 2:0, 3:2}
min(d, key=d.get) //最小 
max(d, key=d.get) //最大

2:利用lambda函数
min(d.items(), key=lambda x: x[1]) 
min(d, key=lambda x: d[x])

======================================
根据value值取对应的键key值:
dic = {'user1':'01', 'user2':'02'} 
a = list(dic.keys())[list(dic.values()).index('01')]
print(a)

======================================
根据value排序
d = {'a':1,'b':4,'c':2}
1.sorted(d.items(),key = lambda x:x[1],reverse = True)

2.f = zip(d.values(),d.keys())
sorted(f)
//结果是 [(1, 'a'), (2, 'c'), (4, 'b')]
======================================
取出字典第一个键值对
1.
sorted(d.items())[0]

2.
>>> d={"a":3,"b":1,"c":5,"d":2}
>>> sorted(d.items())
[('a', 3), ('b', 1), ('c', 5), ('d', 2)]
>>> max(zip(d.values(),d.keys()))
(5, 'c')
>>> min(zip(d.values(),d.keys()))
(1, 'b')
>>> sorted(zip(d.values(),d.keys()))[0]
(1, 'b')
>>>
"""
