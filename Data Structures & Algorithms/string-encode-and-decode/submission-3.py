class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for s in strs:
            sentence += str(len(s)) + "+"+s
        return sentence

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            check = start
            while s[check].isdigit():
                check += 1
            length = int(s[start:check])
            word = s[check + 1: check + 1 + length]
            res.append(word)
            start = check + 1 + length 
        
        return res
        
