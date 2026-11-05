class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        start = 1
        for num in nums:
            arr.append(start)
            start *= num
        
        end = 1
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= end
            end *= nums[j]
        return arr