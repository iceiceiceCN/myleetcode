def getRow(rowIndex):
    if rowIndex ==0:return [1]
    res = [[1]]
    while len(res) < rowIndex +1:
        newRow = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
        res.append(newRow)
    return res[rowIndex]


print(getRow(3))