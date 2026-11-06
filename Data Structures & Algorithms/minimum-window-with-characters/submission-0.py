class Solution:
    def minWindow(self, s: str, t: str) -> str:
        checkS = {}
        checkT = {}
        res = []
        for char in t:
            checkT[char] = checkT.get(char, 0) + 1
            checkS[char] = 0
        have, need = 0, len(checkT)
        l, r = 0, 0 

        while r < len(s):
            if s[r] in checkS:
                checkS[s[r]] += 1
                if checkT[s[r]] == checkS[s[r]]:
                    have += 1
                    
            while have == need:
                if not res or res[1] - res[0] > r - l:
                    res = [l , r]
                if s[l] in checkS:                                  
                    checkS[s[l]] -= 1
                    if checkS[s[l]] < checkT[s[l]]:
                        have -= 1
                l += 1
            r += 1

        if not res:
            return ""
        
        return s[res[0]:res[1] + 1] 