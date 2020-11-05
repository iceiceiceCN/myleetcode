class Solution:
    def countSegments(self, s):
        s = ' ' + s # 加一个空格 保证第一个单词也能计数
        count = 0
        for i in range(1,len(s)):
            if s[i-1] == ' ' and s[i] != ' ':
                count +=1
        return count

"""
计算单词的数量，就等同于计数单词开始的下标个数。
因此，只需要定义好下标的条件，就可以遍历整个字符串，检测每个下标。
定义如下：若该下标前为空格（或者为初始下标），且自身不为空格，则其为单词开始的下标。
该条件可以以常数时间检测。最后，返回满足条件的下标个数。
"""