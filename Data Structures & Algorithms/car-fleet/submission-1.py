class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append([position[i], speed[i]])
        sorted_by_position = sorted(combined, key=lambda x:x[0], reverse=True)
        stack = []
        for i in range(len(sorted_by_position)):
            sp = sorted_by_position[i][1]
            pos = sorted_by_position[i][0]
            time = (target - pos) / sp
            if not stack or stack[-1] < time:
                stack.append(time)
        
        return len(stack)

