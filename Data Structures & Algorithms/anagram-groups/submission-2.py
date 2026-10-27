class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs: 
            check = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                check[index] += 1
            
            if tuple(check) not in res:
                res[tuple(check)] = []
            
            res[tuple(check)].append(word)
        
        ans = []
        for val in res.values():
            ans.append(val)
        return ans