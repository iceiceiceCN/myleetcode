class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        pre = ''
        cur = '1' # 因为第一项为1 所以初始化为1

        # 求第n项，只需要计算n-1次就行，所以range(n-1)
        for i in range(n-1):
            # 此处要把cur赋予pre
            # 因为当前项，就是下一轮迭代的上一轮结果
            pre = cur

            # 每轮计算完后要初始化cur
            cur = ''

            # 定义双指针
            start = 0
            end = 0

            # 开始遍历
            while end <len(pre):
                # 如果遍历到边界的最后一项，需要判断end是否越界，如果越界则跳出循环
                # 统计重复元素的次数(end-start)，直到元素不同时跳出循环
                while end <len(pre) and pre[start] == pre[end]:
                    end += 1

                # 元素出现次数 + 元素
                cur += str(end-start) + pre[start]
                # 更新指针位置，开始统计下一轮
                start = end
            
        return cur