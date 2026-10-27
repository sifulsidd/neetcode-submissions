class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for i, num in enumerate(nums):
            check = target - num
            if check in difference: 
                return [difference[check], i]
            difference[num] = i
        