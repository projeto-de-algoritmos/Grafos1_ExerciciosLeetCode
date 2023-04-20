from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            visited.add(city)
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1
        
        return provinces


"""
Explicando a solução:

1. Iniciamos definindo uma classe Solution com um método findCircleNum que recebe como parâmetro uma matriz isConnected do tipo List[List[int]] e retorna um inteiro.
2. Obtemos o tamanho n da matriz isConnected.
3. Iniciamos um conjunto visited vazio para armazenar as cidades já visitadas.
4. Iniciamos uma variável provinces com valor 0 para armazenar o número de províncias encontradas.
5. Definimos uma função dfs que recebe como parâmetro uma cidade city.
6 .Adicionamos a cidade city ao conjunto visited.
7. Percorremos todas as cidades neighbor de 0 até n-1.
8. Verificamos se a cidade city está diretamente conectada com a cidade neighbor, ou seja, se isConnected[city][neighbor] == 1.
9. Se a cidade neighbor ainda não tiver sido visitada, chamamos a função dfs recursivamente para a cidade neighbor.
10. Percorremos todas as cidades city de 0 até n-1.
11. Se a cidade city ainda não tiver sido visitada, chamamos a função dfs para a cidade city e incrementamos a variável provinces.
12. Retornamos o número total de províncias encontrado em provinces.

Essa solução utiliza uma busca em profundidade (DFS) para percorrer as cidades e encontrar as províncias. A complexidade temporal da solução é O(n^2), já que precisamos percorrer todas as cidades e, para cada cidade, percorrer todas as outras cidades em busca de conexões.
"""