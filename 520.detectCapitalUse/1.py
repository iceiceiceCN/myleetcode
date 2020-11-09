import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if re.match(r'(([A-Z]+)|([A-Z]?[a-z]+))$',word) else False
        return True if re.match(r'(([A-Z]+)$|([A-Z]?[a-z]+)$)',word) else False
        return True if re.match(r'(([A-Z]+$)|([A-Z]?[a-z]+$))',word) else False

# [A-Z]+ :由1个或多个 A-Z字符 组成
# [A-Z]?[a-z]+ : 由0或1个 A-Z字符 + 1个或多个 a-z字符 组成
# $ 表示结尾