class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)

            elif ch == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            
            elif ch == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            
            elif ch == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(float(val1)/val2))
            
            else:
                stack.append(int(ch))
        
        return stack[-1]