class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {}
        for i in range(n):
            tree[i] = []
        
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)
        
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for neighbor in tree[curr]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
        
