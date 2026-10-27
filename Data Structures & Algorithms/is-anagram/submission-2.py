class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        sDic = {}
        tDic = {}

        for i in range(len(s)):
            seenInS = s[i]
            seenInT = t[i]

            if seenInS not in sDic:
                sDic[seenInS] = 0
            sDic[seenInS] += 1

            if seenInT not in tDic:
                tDic[seenInT] = 0
            tDic[seenInT] += 1
        
        return sDic == tDic