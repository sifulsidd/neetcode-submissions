class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for s in strs:
            arr = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                arr[index] += 1
            if tuple(arr) not in check:
                check[tuple(arr)] = []
            check[tuple(arr)].append(s)
        
        return list(check.values())