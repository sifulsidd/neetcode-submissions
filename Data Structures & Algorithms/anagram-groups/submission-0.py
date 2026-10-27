class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDic = {}

        for word in strs:
            arr = [0]  * 26
            for char in word:
                index = ord(char) - ord('a')
                arr[index] += 1
            if tuple(arr) not in anagramDic:
                anagramDic[(tuple(arr))] = []
            anagramDic[tuple(arr)].append(word)
        
        res = []
        for val in anagramDic.values():
            res.append(val)
        return res
