class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = [0] * len(height)

        left = 0
        for h in height:
            left = max(h, left)
            maxLeft.append(left)
        
        right = 0
        for i in range(len(height) - 1, -1, -1):
            right = max(right, height[i])
            maxRight[i] = right
        
        total = 0
        for i in range(len(height)):
            h = min(maxLeft[i], maxRight[i])
            difference = h - height[i]
            total += difference
        return total
