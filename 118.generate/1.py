class Solution(object):
    def generate(self, numRows):
        if numRows ==0:return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res