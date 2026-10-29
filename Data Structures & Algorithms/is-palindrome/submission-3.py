import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())

        l, r = 0, len(cleaned) - 1

        while l < r:
            if not cleaned[l].lower() == cleaned[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
