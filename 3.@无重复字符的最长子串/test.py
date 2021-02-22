class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0
        cur_len = 0
        lookup = []
        left = 0

        for i in range(len(s)):
            cur_len += 1
            if s[i] in lookup:
                cur_len -= 1
                lookup.remove(s[left])
                left += 1
            max_len = max(max_len,cur_len)
            lookup.append(s[i])

            return max_len
a = Solution()
b = a.lengthOfLongestSubstring("abcabcbb")
print(b)