class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceArray = {}

        for i in range(len(nums)):
            number = nums[i]
            difference = target - number 
            if difference in differenceArray:
                return [differenceArray[difference], i]
            differenceArray[number] = i
        