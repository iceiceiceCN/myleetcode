class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            for k in range(len(row)):
                row[k] = 1 - row[k]
            
            i = 0
            j = len(row)-1

            while i<j:
                row[i],row[j] = row[j],row[i]
                i +=1
                j -=1
        return A

"""
时间复杂度 O(N)，做了两次遍历，而O(2N) = O(N)
空间复杂度 O(1)，只用了常量空间，没有用额外的空间
"""