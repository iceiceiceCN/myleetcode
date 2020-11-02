from functools import reduce
def addToArrayForm(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    A = list(str(reduce(lambda a,b:a*10+b,A) + K))
    return A 
    #  (str(reduce(lambda a,b:a*10+b,A) + K)) : '1234'
    # list(str(reduce(lambda a,b:a*10+b,A) + K)) ['1', '2', '3', '4']

A = [1,2,0,0]
K = 34
addToArrayForm(A,K)
# reduce(f(a,b), nums) = f(...f(f(nums[0],nums[1]),nums[2]),...,nums[-1])