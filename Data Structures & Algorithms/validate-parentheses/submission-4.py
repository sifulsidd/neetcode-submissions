class Solution:
    def isValid(self, s: str) -> bool:
        closed = {")":"(",
                 "}":"{",
                 "]":"["}

        check = []
        for ch in s:
            if ch not in closed:
                check.append(ch)
            else:
                if not check:
                    return False
                popped = check.pop()
                if closed[ch] != popped:
                    return False
        
        return not check