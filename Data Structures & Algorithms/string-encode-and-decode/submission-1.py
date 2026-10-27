class Solution:

    def encode(self, strs: List[str]) -> str:
        decodedMessage = ""
        for word in strs:
            decodedMessage += str(len(word)) + "%" + word
        return decodedMessage



    def decode(self, s: str) -> List[str]:
        res = []
        # s[0:1] = %
        i = 0

        while i < len(s):
            j = i 
            # keep incrementing j until we reach our delimeter
            while s[j] != "%":
                j += 1
            # how many following characters after j to get the characters 
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            # beginning of next string or end of string
            i = j + 1 + length
        return res