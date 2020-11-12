import itertools


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            seen = set()
            for i in A:
                if i in seen:
                    return True
                seen.add(i)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) > 2:
                    return False

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


"""
能够满足题意的只有两种情况：
1. A = B 且【有>=2个相同的字符】。 比如"ab"与"ba"就不行，但是"aab"与"aba"就可以。

2. A != B且【只有2处不同，并且不同的地方要求A[i] = B[j],A[j] = B[i]】,
换句话说不同的地方只能是位置颠倒。

"""
