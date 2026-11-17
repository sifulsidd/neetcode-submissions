class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, total, res):
            if i == len(nums) or total > target:
                return 
            if total == target:
                ans.append(res.copy())
                return
            res.append(nums[i])
            backtrack(i, total + nums[i], res)
            res.pop()
            backtrack(i + 1, total, res)
        backtrack(0, 0, [])
        return ans
        