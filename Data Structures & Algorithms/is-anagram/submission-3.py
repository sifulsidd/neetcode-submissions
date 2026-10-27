class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        checkS = {}
        checkT = {}
        
        for char in s:
            if char not in checkS:
                checkS[char] = 0
            checkS[char] += 1
        
        for char in t:
            if char not in checkT:
                checkT[char] = 0
            checkT[char] += 1
        
        return checkS == checkT


        