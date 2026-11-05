class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            if num - 1 in s:
                continue
            length = 1
            while num + 1 in s:
                length += 1
                num += 1
            res = max(length, res)
        
        return res