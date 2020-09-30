# # for i in range(1,5):
# #     print(i)
# res = [[1],[1,1],[1,2,1]]
# print([0]+res[-1])
# print(res[-1]+[0])

# print(zip([0]+res[-1],res[-1]+[0]))

# row = [a+b for a,b in zip([0]+res[-1],res[-1]+[0])]
# print(row)

# numRows =5
# ans = [[1]*i for i in range(numRows+1)]
# print(ans)

row_num = 5
row = [None for _ in range(row_num+1)]
print(row)