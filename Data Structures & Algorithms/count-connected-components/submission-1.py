class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(curr):
            if curr in visit:
                return 0 
            visit.add(curr)
            for neighbor in adj[curr]:
                dfs(neighbor)
            return 1 
        
        res = 0
        for i in range(n):
            if i not in visit:
                res += dfs(i)
        return res