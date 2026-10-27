class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums) + 1)] 
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for key, val in dic.items():
            res[val].append(int(key))
        ans = []
        for i in range(len(res) -1, 0, -1):
            for n in res[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        