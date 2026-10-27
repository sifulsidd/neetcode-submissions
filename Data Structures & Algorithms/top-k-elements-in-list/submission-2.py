class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums) + 1)]
        check = {}

        for num in nums:
            if num not in check:
                check[num] = 0
            check[num] += 1
        
        for key,val in check.items():
            res[val].append(int(key))
        
        ans = []
        for i in range(len(res) - 1, -1, -1):
            # print(res[i])
            check = len(res[i])
            # print(res[i])
            if check > 0:
                ans.extend(res[i])
                if len(ans) == k:
                    return ans
