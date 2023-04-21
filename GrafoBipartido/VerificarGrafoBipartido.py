from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n

        for u in range(n):
            if color[u] == 0:
                color[u] = 1
                queue = deque([u])

                while queue:
                    v = queue.popleft()
                    for w in graph[v]:
                        if color[w] == 0:
                            color[w] = 3 - color[v] 
                            queue.append(w)
                        elif color[w] == color[v]:
                            return False

        return True

"""
Explicação do Algoritmo:
Para verificar se o gráfico é bipartido utilizei a vericação em duas cores,
colorindo um nó com a cor 1 e os seus vizinhos com a cor 2. Se o nó vizinho
tem a mesma cor, então o grafo não é bipartido.

1. Inicializei um matriz de cores de tamanho n.
2. Para cada nó não colorido u no grafo, pintei u com a cor 1.
3. Inicializei a fila e coloquei u na fila.
4. E enquanto a fila não estiver vazia, desenfilerei um nó v.
5. Para cada vizinho w e v, se w não estiver colorido, ele é pintado com a cor oposta a de v e
é colocado na fila. Se w estiver pintado com a mesma cor que v, é onde retorna false (não bipartido).
6. Se todos os nós forem coloridos sem conflitos, retorna true (bipartido)
"""