class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        def backtrack(i, curr):
            if i == len(word):
                return curr.end
            
            if word[i] == ".":
                for child in curr.children.values():
                    if backtrack(i + 1, child):
                        return True

            if word[i] not in curr.children:
                return False
            
            return backtrack(i + 1, curr.children[word[i]])
        return backtrack(0, self.root)
