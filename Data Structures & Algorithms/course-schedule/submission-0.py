class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {}
        for i in range(numCourses):
            preReq[i] = []

        for cur, pre in prerequisites:
            preReq[cur].append(pre)

        visit = set()
        def dfs(curr):
            if curr in visit:
                return False
            
            if not preReq[curr]:
                return True 

            visit.add(curr)
            for nei in preReq[curr]:
                if not dfs(nei):
                    return False
            visit.remove(curr)
            preReq[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        