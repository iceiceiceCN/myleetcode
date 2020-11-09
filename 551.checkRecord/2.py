class Solution:
    def checkRecord(self, s: str) -> bool:
        A_num, L_num = 0, 0
        for a in s:
            if a == "A":
                A_num += 1
                if A_num >= 2: return False
                L_num = 0
            elif a == "L":
                L_num += 1
                if L_num >= 3: return False
            else:
                L_num = 0
        return True