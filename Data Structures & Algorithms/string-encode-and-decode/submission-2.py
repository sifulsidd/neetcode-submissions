class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "$" + word
        return res


    def decode(self, s: str) -> List[str]:
        start = 0

        ans = []
        while start < len(s):
            check = start
            while s[check] != "$":
                check += 1
            size = int(s[start:check])
            word = s[check + 1: check + 1 + size]
            start = check + 1 + size
            ans.append(word)
        return ans
    