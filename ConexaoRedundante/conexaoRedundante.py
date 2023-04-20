# ATENÇÃO
# ESSA RESOLUÇÃO NÃO ESTÁ 100% CORRETA

from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(node, parent):
            nonlocal cycle
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    cycle = [neighbor, node]
                    return
                else:
                    dfs(neighbor, node)
                if cycle:
                    return
        
        # Step 1: Create graph and detect possible roots
        graph = {}
        roots = set()
        for u, v in edges:
            if v in graph:
                roots.discard(v)
                roots.add(u)
            else:
                graph[v] = []
                roots.add(u)
            graph[u] = graph.get(u, []) + [v]
        
        # Step 2: Detect cycle and find edge to remove
        cycle = None
        visited = set()
        for root in roots:
            dfs(root, None)
            if cycle:
                break
        
        # Step 3: Return edge to remove
        for u, v in reversed(edges):
            if v == cycle[0] and u == cycle[1]:
                return [u, v]
        return cycle