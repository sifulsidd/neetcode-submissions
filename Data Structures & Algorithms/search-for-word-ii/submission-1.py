class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def addWord(word, curr):
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end = True
        
        root = TrieNode()
        for word in words:
            addWord(word, root)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 
                or c == COLS or r == ROWS or 
                (r,c) in visit 
                or board[r][c] not in node.children):
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
        