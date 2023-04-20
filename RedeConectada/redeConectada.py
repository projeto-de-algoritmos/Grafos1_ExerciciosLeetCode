from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                stack = [i]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        stack += graph[node]
        
        return components - 1

"""
Explicando a solução:

O método makeConnected recebe dois argumentos: o número n de computadores e a lista connections com as conexões entre eles. Primeiramente, verificamos se há conexões suficientes para conectarmos todos os computadores. Se o número de conexões for menor do que n - 1, não será possível conectar todos os computadores e o método retorna -1.

Em seguida, construímos o grafo a partir da lista connections. Para cada par de nós (u, v) na lista, adicionamos uma aresta de u para v e uma aresta de v para u.

Depois, percorremos o grafo para contar o número de componentes conexos. Para cada nó i que ainda não foi visitado, incrementamos o contador de componentes e percorremos o componente conexo de i utilizando uma busca em profundidade.

Por fim, retornamos o número de componentes conexos menos 1, que é o número mínimo de vezes que precisamos fazer a operação de "extrair cabos" para conectar todos os computadores.
"""