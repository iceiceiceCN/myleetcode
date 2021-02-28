class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1,num2=num2,num1
        
        num2 = '0' * (len(num1) - len(num2)) + num2
        res = ''
        summ = 0
        for i in range(len(num1)):
            n1 = int(num1[-i-1])
            n2 = int(num2[-i-1])
            r = (n1+n2+summ)%10
            summ = (n1+n2+summ)//10
            res = str(r) + res

        if summ == 1:
            res = '1' + res

        return res

if __name__ == "__main__":
    A = Solution()
    B = A.addStrings("9", "9")
    print(B)