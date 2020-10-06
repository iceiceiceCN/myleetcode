class Solution(object):
    def generate(self, numRows):
        ans = [[1]*i for i in range(1,numRows+1)] # 如果是range(numRows+1)的话，会出现一个空子数组，[[],[1],[1,1]]
        for line in range(2,numRows): # 第一行是[1],第二行是[1,1],只用从第三行(索引为2)开始,一直到第numRows行(索引为numRows-1)
            for col in range(1,line):
                ans[line][col] = ans[line-1][col] + ans[line-1][col-1]
        return ans