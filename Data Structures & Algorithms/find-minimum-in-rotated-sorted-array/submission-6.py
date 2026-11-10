class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minVal = float("inf")
        while l <= r:
            m = (l + r) // 2
            minVal = min(nums[m], minVal)
            if nums[l] < nums[r]:
                minVal = min(nums[l], minVal)
                break
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        
        return minVal
