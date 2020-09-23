class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits
"""
遇到加减的题一定要考虑 9 的加减，和进位问题。
"""
