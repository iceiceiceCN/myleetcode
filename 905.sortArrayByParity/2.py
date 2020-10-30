def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    return ([x for x in A if x%2==0 ]+[x for x in A if x%2==1])

A = [3,1,2,4]
B = sortArrayByParity(A)
print(B)

"""
第一遍输出偶数，第二遍输出奇数。
时间复杂度：O(N)，其中 N 是 A 的长度。
空间复杂度：O(N)，存储结果的数组。
"""