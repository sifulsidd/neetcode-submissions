class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        multiple = 1
        for i in range(len(nums)):
            res[i] *= multiple
            multiple *= nums[i]
        
        multipleBack = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= multipleBack 
            multipleBack *= nums[j]
        return res