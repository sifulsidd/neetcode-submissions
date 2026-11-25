class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return 0 
            visit.add(curr)
            for neighbor in adj[curr]:
                if prev == neighbor:
                    continue
                dfs(neighbor, curr)
            return 1 
        res = 0
        for i in range(n):
            if i in visit:
                res += 0
            res += dfs(i, -1)
        return res