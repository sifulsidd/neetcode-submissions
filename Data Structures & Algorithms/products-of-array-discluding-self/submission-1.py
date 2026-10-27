class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        left = 1
        for num in nums:
            curr = num 
            res.append(left)
            left *= curr
        right = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= right
            right *= nums[j]
        return res

