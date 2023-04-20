# [Número de Províncias](https://leetcode.com/problems/number-of-provinces/)

## Nível: Médio

Existem `n` cidades. Algumas delas estão conectadas, enquanto outras não. Se a cidade `a` está conectada diretamente com a cidade `b`, e a cidade `b` está conectada diretamente com a cidade `c`, então a cidade `a` está conectada indiretamente com a cidade `c`.

Uma **província** é um grupo de cidades conectadas direta ou indiretamente e nenhuma outra cidade fora do grupo.

Você recebe uma `n x n` matriz `isConnectedonde` em que `isConnected[i][j] = 1` se a `iª` cidade e a `jª` cidade estão diretamente conectadas e, caso contrário, `isConnected[i][j] = 0`

Retorne o número total de **províncias**.


**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

``` bash
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

``` bash
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```