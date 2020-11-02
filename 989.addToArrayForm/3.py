def addToArrayForm( A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    # A[-1] += K
    # for i in range(len(A) - 1, -1, -1):
    #     carry, A[i] = divmod(A[i], 10) # divmod -> 得到 (商,余数)
    #     if i: A[i-1] += carry
    # if carry:
    #     A = map(int, str(carry)) + A # 1000 + [0] -> [1,0,0,0] + [0] -> [1,0,0,0,0]


    tmp_carry = K
    for i in range(len(A)):
        A[-1-i] = A[-1-i] + tmp_carry
        tmp_stay = A[-1-i] %10
        tmp_carry = A[-1-i] //10
        A[-1-i] = tmp_stay
    if tmp_carry:
        tmp = map(int,str(tmp_carry))
        A = tmp +A
    
    return A




A = [0]
K = 10000
addToArrayForm(A,K)
