# [Número de Operações para Tornar a Rede Conectada](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

**Nível: Médio**

São `n` computadores numerados de `0` a `n - 1` conectados por cabos de internet `connections` formando uma rede onde `connections[i] = [aᵢ, bᵢ]` representa uma conexão entre computadores `aᵢ` e `bᵢ`. Qualquer computador pode alcançar qualquer outro computador direta ou indiretamente através da rede. 

Você recebe uma rede inicial de computadores `connections`. Você pode extrair certos cabos entre dois computadores conectados diretamente e colocá-los entre qualquer par de computadores desconectados para torná-los conectados diretamente.

Retorne o número mínimo de vezes que você precisa fazer isso para conectar todos os computadores. Se não for possível, retorne `-1`.


**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png)

``` bash
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explicação: Remova o cabo entre os computadores 1 e 2 e coloque entre os computadores 1 e 3.
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png)

``` bash
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

**Exemplo 3:**

``` bash
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explicação: Não há cabos suficientes.
```