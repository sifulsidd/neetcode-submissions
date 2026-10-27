class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            check = [0] * 26
            for char in string: 
                index = ord(char) - ord('a')
                check[index] += 1
            c = tuple(check)
            if c not in res:
                res[c] = []
            res[c].append(string)
        
        ans = []
        for key, val in res.items():
            ans.append(val)
        return ans