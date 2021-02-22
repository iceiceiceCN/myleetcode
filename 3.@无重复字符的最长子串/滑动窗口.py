class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        cur_len = 0
        lookup = []
        n = len(s)
        left = 0

        for i in range(n):
            cur_len += 1
            if s[i] in lookup: # 如果遇到"pww" 我们需要使用 *while* 进行多次判断，全部清除掉。
                cur_len -= 1
                lookup.remove(s[left]) # 因为是滑动窗口，必须严格*从左到右挨个移除*。如果用lookup.remove(s[i])的话，有可能删除的是右边的元素。
                # lookup.remove(s[i]) # 错误写法
                left += 1
            max_len = max(max_len, cur_len)
            lookup.append(s[i])

        return max_len

a = Solution()
b = a.lengthOfLongestSubstring("abcabcbb")
print(b)

# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/