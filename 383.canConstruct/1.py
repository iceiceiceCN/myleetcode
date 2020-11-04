class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_hash = {}
        for i,val in enumerate(magazine):
            if val in magazine_hash:
                magazine_hash[val] +=1
            else:
                magazine_hash[val] = 1

        for i,val in enumerate(ransomNote):
            if val in magazine_hash and magazine_hash[val] > 0:
                magazine_hash[val] -=1
            else:
                return False
        
        return True

# 1. 用哈希表存储magazine字符及个数
# 2. 遍历ransomNote:
#   2.1. 如果哈希表中有该字符并且字符计数大于零，说明仍能由magzine构成，此时对应的字符计数减一
#   2.2. 否则，无法构成，返回False
# 时间复杂度: O(N) - N（遍历magazine） + 1（字典检索为O(1)）
# 空间复杂度: O(N)