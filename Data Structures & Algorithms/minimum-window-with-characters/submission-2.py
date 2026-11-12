class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        check = {}
        has = {}
        res = []
        for char in t:
            if char not in check:
                check[char] = 0
            check[char] += 1
            if char not in has:
                has[char] = 0
        need = len(check)
        have = 0
        minLength = float('inf')
        res = ""
        l, r = 0, 0
        while r < len(s):
            if s[r] in has:
                has[s[r]] += 1
                if has[s[r]] == check[s[r]]:
                    have += 1
                while have == need:
                    if r - l + 1 < minLength:
                        res = s[l:r + 1]
                        minLength = r - l + 1
                    if s[l] in has:
                        has[s[l]] -= 1
                        if has[s[l]] < check[s[l]]:
                            have -= 1
                    l += 1
            r += 1
        return res
        

