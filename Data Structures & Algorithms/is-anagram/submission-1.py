class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        if len(s) != len(t): return False
        for char in s:
            if char not in check:
                check[char] = 0
            check[char] += 1
        
        for char in t:
            if char not in check or check[char] == 0:
                return False
            check[char] -= 1
        
        for char in s:
            if check[char] > 0:
                return False
        
        return True