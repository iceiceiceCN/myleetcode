class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','{':'}','[':']'}

        for i in s:
            if i in dic:
                stack.append(i)
            
            else:
                if not stack or i != dic[stack[-1]]:
                    return False
                stack.pop()
        
        return not stack

a = Solution()
b = a.isValid("()")