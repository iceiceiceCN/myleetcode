class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        if A == B:
            check = set()
            for i in A:
                if i not in check:
                    check.add(i)
                else:
                    return True
            return False
        count, tmp = 0, []
        for i in range(len(A)):
            if A[i] != B[i]:
                tmp.append(A[i])
                tmp.append(B[i])
                count += 1
            if count == 3:
                return False
        if count != 2:
            return False
        if tmp[0] == tmp[3] and tmp[1] == tmp[2]:
            return True
        return False
