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
        def dfs(i, curr):
            # first check if we have the same length of word, return the curr.end value
            if i == len(word):
                return curr.end
            
            # if the character is "." we have to check each children and move one to the next child 
            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
            # if character not in children, return false
            if word[i] not in curr.children:
                return False
            
            return dfs(i + 1, curr.children[word[i]])
        return dfs(0, self.root)
