from typing import List

class Solution:
    
    # Função auxiliar para encontrar o ancestral de um nó
    def findParent(self, v: int, parent: List[int]) -> int:
        if parent[v] == 0: 
            parent[v] = v 
        
        # Caso contrário, encontra o ancestral de v recursivamente e atualiza parent[v]
        if parent[v] != v:
            parent[v] = self.findParent(parent[v], parent)
        
        return parent[v] # Retorna o ancestral de v

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Precisamos garantir que cada nó tenha apenas um pai e que não haja ciclos nesse grafo direcionado
        
        n = len(edges)
        map = [0] * (n + 1) # Mapa para rastrear os pais de cada nó
        
        ans1, ans2 = None, None # Armazenam as duas arestas redundantes (se houver)

        # Etapa 1: Identificar uma aresta redundante com base no mapa
        for edge in edges:
            u, v = edge[0], edge[1]
            
            if map[v] > 0:
                ans1 = [map[v], v] 
                ans2 = edge 
            
            map[v] = u # Registra u como pai de v no mapa

        # Etapa 2: Encontrar ciclos e arestas redundantes usando a técnica de união e busca (Union-Find)
        parent = [0] * (n + 1) 

        for edge in edges:
            if edge == ans2: # Ignorar a segunda aresta redundante
                continue
            
            u, v = edge[0], edge[1]
            
            pu = self.findParent(u, parent) 
            pv = self.findParent(v, parent) 
            
            if pu == pv:
                return ans1 if ans1 is not None else edge # Retorna a primeira aresta redundante, se houver, caso contrário retorna a aresta atual
            
            parent[pv] = u # Une o conjunto que contém v com o conjunto que contém u

        return ans2 # Retorna a segunda aresta redundante

    
"""
Explicando a solução:
1. O código cria uma função auxiliar para encontrar o pai de um vértice em uma árvore de pais.
2. Ele inicializa duas variáveis como nulas.
3. O código percorre cada aresta em edges, verificando se o vértice de destino já possui um 
pai atribuído.
4. Se sim, armazena a primeira aresta encontrada que torna o grafo inválido em ans1 e ans2.
5. Caso contrário, o pai do vértice é definido como o vértice de origem da aresta atual.
6. O código cria uma matriz de pais e itera através de cada aresta novamente.
7. Se a aresta atual for a mesma que foi armazenada em ans2, o loop é interrompido.
8. Caso contrário, o código encontra o pai de cada vértice e verifica se eles são iguais.
9. Se eles são iguais, isso significa que há um ciclo no grafo, então retorna ans1 
se ela existir.
10. Caso contrário, retorna a aresta atual (ans2).
11. Se os pais forem diferentes, o pai do vértice de destino é definido como o vértice 
de origem, realizando a união dos conjuntos.
12. Por fim, o código retorna ans2.
"""