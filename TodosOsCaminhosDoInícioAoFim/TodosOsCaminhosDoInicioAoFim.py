class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        all_paths = []

        def dfs(node, path):
            path.append(node)
            if node == n-1:
                all_paths.append(path)
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path.copy())

        dfs(0, [])
        return all_paths
