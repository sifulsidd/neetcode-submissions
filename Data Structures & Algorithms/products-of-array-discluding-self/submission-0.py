class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        left = 1
        for i in range(len(nums)):
            curr = nums[i]
            prefix.append(left)
            left *= curr 
        
        postfix = [1 for _ in range(len(nums))]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            postfix[i] = right
            right *= curr
        
        for i in range(len(nums)):
            nums[i] = postfix[i] * prefix[i]
        return nums

        
            
