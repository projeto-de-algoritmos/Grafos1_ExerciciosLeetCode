# [Todos os Caminhos do Início ao Fim](https://leetcode.com/problems/all-paths-from-source-to-target/)

**Nível: Médio**

Dado um grafo acíclico direcionado (**DAG**) de `n` nós rotulados de `0` a `n-1`, encontre todos os caminhos possíveis do nó `0` ao nó `n-1` e retorne-os em qualquer ordem.

O grafo é fornecido da seguinte forma: `graph[i]` é uma lista de todos os nós que você pode visitar a partir do nó `i` (ou seja, existe uma aresta direcionada do nó `i` para o nó `graph[i][j]`).

**Exemplo 1**
![App Screenshot](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)
``` bash
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explicação: Existem dois caminhos: 0 -> 1 -> 3 e 0 -> 2 -> 3.
```


**Exemplo 2**
![App Screenshot](https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg)
```bash
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```