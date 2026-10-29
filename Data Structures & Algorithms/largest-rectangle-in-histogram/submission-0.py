class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # [height, index]
        maxArea = 0
        for i, h  in enumerate(heights):
            start = i
            while len(stack) > 0 and h < stack[-1][0]:
                height, index = stack.pop()
                area = height * (i - index)
                maxArea = max(area, maxArea)
                start = index
            stack.append([h, start])
            
        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
            