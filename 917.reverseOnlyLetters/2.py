class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        left,right=0,len(S)-1

        while left<right:
            if S[left].isalpha() and S[right].isalpha():
                S[left],S[right] = S[right],S[left]
                left += 1
                right -= 1
            elif not S[left].isalpha() and S[right].isalpha():
                left += 1
            elif S[left].isalpha() and not S[right].isalpha():
                right -= 1
            elif not S[left].isalpha() and not S[right].isalpha():
                left += 1
                right -= 1

        return ''.join(S)

"""
双指针法
"""