class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        l, r = 0, 0
        maxLength = 0
        while r < len(s):
            check[s[r]] = check.get(s[r], 0) + 1
            while check[s[r]] > 1:
                check[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength