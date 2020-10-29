def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    r = len(A)
    c = len(A[0])
    A_copy = A[:]
    A = []
    temp = []
    for c1 in range(c):
        for r1 in range(r):
            temp.append(A_copy[r1][c1])
        A.append(temp)
        temp = []
    return A


A = [[1,2,3],[4,5,6],[7,8,9]]
transpose(A)