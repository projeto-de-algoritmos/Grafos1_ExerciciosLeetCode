# Verificação de Grafo Bipartido

Existe um grafo não direcionado com `n` nós, onde cada nó é numerado entre 0 e n - 1. É fornecido um array 2D chamado de "graph", onde `graph[u]` é um array de nós aos quais o nó `u` é adjacente. De forma mais formal, para cada `v` em `graph[u]`, existe uma aresta não direcionada entre o nó `u` e o nó `v`. O grafo possui as seguintes propriedades:

- Não existem autoarestas (`graph[u]` não contém `u`).

- Não existem arestas paralelas (`graph[u]` não contém valores duplicados).

- Se `v` está em `graph[u]`, então `u` está em `graph[v]` (o grafo é não direcionado).

- O grafo pode não ser conectado, o que significa que pode haver dois nós `u` e `v` para os quais não há caminho entre eles.

Um grafo é bipartido se os nós puderem ser divididos em dois conjuntos independentes `A` e `B`, de modo que cada aresta no grafo conecte um nó no conjunto `A` e um nó no conjunto `B`.

Return `true` se e somente se o grafo for bipartido.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg)

``` bash
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explicação: Não há como particionar os nós em dois conjuntos independentes de modo que cada aresta conecte um nó em um conjunto e outro nó no outro conjunto.
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)

``` bash
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explicação: Podemos particionar os nós em dois conjuntos: {0, 2} e {1, 3}.
```