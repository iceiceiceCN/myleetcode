def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    return (all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1)))

A=[11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
isMonotonic(A)