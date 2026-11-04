class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in difference:
                return [difference[diff], i]
            difference[num] = i
        