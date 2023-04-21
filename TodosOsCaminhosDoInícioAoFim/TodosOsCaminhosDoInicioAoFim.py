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

"""
1. Inicializamos uma lista vazia de caminhos all_paths para armazenas os caminhos 
possíveis do nó 0 ao nó n-1.
2. Definimos uma função auxilia dfs que recebe o nó atual como entrada. E é uma lista
de nós visitados até o momento.
3. Na função dfs, é adicionado o nó atual ao caminho.
4. Se o nó atual for igual a n-1, o caminho atual é adicionado ao all_paths.
5. Se não, para cada nó vizinho no graph[node], chamamos a função dfs recursiva com
vizinho como novo nó e uma cópia do caminho atual como novo caminho.
6. Por fim, é chamada a função dfs com o nó 0 e um lista vazia como caminho.
7. É retornado a lista all_paths
"""