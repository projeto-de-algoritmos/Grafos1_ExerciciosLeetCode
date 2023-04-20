# [Conexão Redundante II](https://leetcode.com/problems/redundant-connection-ii/)

**Nível: Difícil**

Neste problema, uma árvore enraizada é um grafo **direcionado** tal que existe exatamente um nó (a raiz) para o qual todos os outros nós são descendentes desse nó, além de cada nó ter exatamente um pai, exceto o nó raiz que não possui pais.

A entrada fornecida é um grafo direcionado que começou como uma árvore enraizada com `n` nós (com valores distintos de `1` a `n`), com uma aresta direcionada adicional adicionada. A aresta adicionada tem dois vértices diferentes escolhidos de `1` a `n`, e não era uma aresta que já existia.

O gráfico resultante é dado como uma matriz 2D de `edges`. Cada elemento de `edges` é um par `[uᵢ, vᵢ]` que representa uma aresta **direcionada** conectando nós `uᵢ` e `vᵢ`, onde `uᵢ` é um pai do filho `vᵢ`.

Retorne *uma aresta que pode ser removida para que o grafo resultante seja uma árvore enraizada de `n` nós*. Se houver várias respostas, retorne a resposta que ocorrer por último na matriz 2D fornecida.


**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg)

``` bash
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg)

``` bash
Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]
```