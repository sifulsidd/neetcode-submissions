class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        check = defaultdict(int)
        maxF = 0 
        res = 0
        l, r = 0 , 0 

        while r < len(s):
            check[s[r]] = 1 + check.get(s[r], 0)
            
            maxF = max(check[s[r]], maxF)

            while (r - l + 1) - maxF > k:
                check[s[l]] -= 1
                l += 1
            windowLen = r - l + 1
            res = max(windowLen, res)
            r += 1
        
        return res
