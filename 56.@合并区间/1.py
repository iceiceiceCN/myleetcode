class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        res = [intervals.pop(0)]

        while intervals:
            tmp = intervals.pop(0)
            if tmp[0] <= res[-1][1] < tmp[1]:
                res[-1][1] = tmp[1]
            elif res[-1][1] < tmp[0]:
                res.append(tmp)

        return res


a = Solution()
b = a.merge([[1, 4], [4, 5]])
print(b)
