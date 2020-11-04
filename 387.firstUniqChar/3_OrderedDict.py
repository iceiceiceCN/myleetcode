from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        odcit = OrderedDict()

        for i, val in enumerate(s):
            if val in odcit:
                odcit[val] += 1
            else:
                odcit[val] = 1

        for k, v in odcit.items(): # 必须要使用odcit.items() 才能得到有序字典，不能用enumerate(odict),使用后者的话得到的字典还是无序的。
            if v == 1:
                return s.index(k)

        return -1

if __name__ == "__main__":
    A = Solution()
    B = A.firstUniqChar("leetcode")

"""
import collections
print "Regular dictionary"
d={}
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print k,v
print "\nOrder dictionary"
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['1'] = '1'
d1['2'] = '2'
for k,v in d1.items():
    print k,v

输出：
Regular dictionary
a A
c C
b B

Order dictionary
a A
b B
c C
1 1
2 2

可以看到，同样是保存了ABC等几个元素，但是使用OrderedDict会根据放入元素的先后顺序进行排序。所以输出的值是排好序的。
OrderedDict对象的字典对象，如果其顺序不同那么Python也会把他们当做是两个不同的对象，请看事例：

print 'Regular dictionary:'
d2={}
d2['a']='A'
d2['b']='B'
d2['c']='C'

d3={}
d3['c']='C'
d3['a']='A'
d3['b']='B'

print  d2==d3

print 'OrderedDict:'
d4=collections.OrderedDict()
d4['a']='A'
d4['b']='B'
d4['c']='C'

d5=collections.OrderedDict()
d5['c']='C'
d5['a']='A'
d5['b']='B'

print  d4==d5

输出：
Regular dictionary:
True

OrderedDict:
False

再看几个例子：
dd = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
#按key排序
kd = collections.OrderedDict(sorted(dd.items(), key=lambda t: t[0]))
print kd
#按照value排序
vd = collections.OrderedDict(sorted(dd.items(),key=lambda t:t[1]))
print vd

#输出
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
"""