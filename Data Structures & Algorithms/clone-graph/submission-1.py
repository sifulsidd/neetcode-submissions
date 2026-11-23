"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # if node exists in hashmap just return that node
            if node in oldToNew:
                return oldToNew[node]
            # create the new node with the val at the current node
            copy = Node(node.val)
            # map the old node to the copy 
            oldToNew[node] = copy

            # make copy of neighbors
            for neighbor in node.neighbors:
                # append neighbors to copy node
                copy.neighbors.append(dfs(neighbor))
            return copy 
        return dfs(node) if node else None 