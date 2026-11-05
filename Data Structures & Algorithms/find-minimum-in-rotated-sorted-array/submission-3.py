class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                
            m = (l + r) // 2
            minVal = min(nums[m], minVal)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1 
        
        return minVal
