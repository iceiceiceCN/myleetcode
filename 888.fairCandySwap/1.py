class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        Sa,Sb = sum(A),sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb-Sa)/2 in setB:
                return [x,x + (Sb-Sa)/2]


"""
设爱丽丝和鲍勃分别总计有Sa,Sb的糖果。
如果爱丽丝给了糖果 x，并且收到了糖果 y，那么鲍勃收到糖果 x 并给出糖果 y。那么，我们一定有Sa - x + y = Sb + x -y
对于公平的糖果交换。这意味着 y = x + (Sb-Sa)/2
我们的策略很简单。对于爱丽丝拥有的每个糖果 x，如果鲍勃有y = x + (Sb-Sa)/2的糖果，我们就返回[x，y]。
我们在常量时间内使用集 Set 结构来检查鲍勃是否拥有所需的糖果 y。
"""