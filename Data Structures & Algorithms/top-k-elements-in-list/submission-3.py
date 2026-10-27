class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for _ in range(len(nums) + 1)]

        check = {}

        for num in nums:
            if num not in check:
                check[num] = 0
            check[num] += 1
        
        for key, val in check.items():
            res[val].append(key)
        
        answer = []
        for i in range(len(nums), -1, -1):
            if not res[i]:
                continue
            answer.extend(res[i])
            if len(answer) == k:
                return answer
