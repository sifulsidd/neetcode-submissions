class Solution:
    def isValid(self, s: str) -> bool:
        check = {")" : "(", 
                 "}":"{", 
                 "]":"["}

        stack = []

        for ch in s:
            if ch in check:
                if len(stack) == 0:
                    return False
                compare = stack.pop()  
                if not check[ch] == compare:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0