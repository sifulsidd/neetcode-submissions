class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = float("inf")
        for word in strs:
            shortest = min(len(word), shortest)
        
        for i in range(shortest):
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
            prefix += s[i]
        return prefix
        