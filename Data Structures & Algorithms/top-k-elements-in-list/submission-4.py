class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}

        for num in nums:
            check[num] = check.get(num, 0) + 1 

        arr = [[] for i in range(len(nums) + 1)]

        for key,val in check.items():
            arr[val].append(key)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            if not arr[i]:
                continue
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res