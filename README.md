# 💰 Análise de Algoritmos para o Problema da Troca de Moedas

Este projeto implementa e compara quatro abordagens algorítmicas para resolver o "Problema da Troca de Moedas" (Coin Change Problem), um clássico problema de otimização. O objetivo é encontrar a menor quantidade de moedas para formar um montante `M` usando um conjunto ilimitado de moedas de determinados valores.

**Integrantes do Grupo:** 🧑‍💻
- João Victor Soave (RM557595)
- Maria Alice Freitas Araújo (RM557516)
- Ianny Raquel Ferreira de Souza (RM559090)

## 1. O Problema da Troca de Moedas 🪙

O problema consiste em, dado um montante `M` e um conjunto de moedas com valores `{c1, c2, ..., ck}`, determinar o número mínimo de moedas cuja soma é exatamente `M`.

- **Natureza do Problema:** É um problema de otimização combinatória, pois busca a "melhor" solução (a que usa menos moedas) dentre um conjunto de combinações possíveis.

### Programação Dinâmica (PD) 🧠
A Programação Dinâmica é uma técnica poderosa para resolver problemas que podem ser divididos em subproblemas menores. Ela se baseia em dois pilares:

1.  **Subestrutura Ótima:** A solução ótima para o montante `M` pode ser encontrada a partir das soluções ótimas de subproblemas menores (por exemplo, `M - valor_da_moeda`).
2.  **Subproblemas Sobrepostos:** Durante o cálculo, os mesmos subproblemas são resolvidos múltiplas vezes. A PD armazena o resultado desses subproblemas (usando memoização ou tabulação) para evitar recálculos, tornando o algoritmo eficiente.

---

## 2. Análise Detalhada das Abordagens ⚙️

Foram implementadas quatro funções em Python, cada uma representando uma abordagem diferente para o problema.

### Função 1: Estratégia Gulosa (Iterativa) - `qtdeMoedas`
- **Conceito:** A abordagem gulosa tenta resolver o problema fazendo a escolha localmente ótima em cada etapa. Neste caso, ela ordena as moedas em ordem decrescente e, a cada passo, pega o maior número possível da maior moeda que "cabe" no valor restante.
- **Análise Crítica:** Esta estratégia **não garante** a solução ótima para todos os conjuntos de moedas. Ela funciona para sistemas canônicos (como o Real ou Dólar), mas falha em outros casos.
- **Demonstração de Falha ❌:**
  - `M = 6`, `moedas = [1, 3, 4]`
    - **Solução Gulosa:** `4 + 1 + 1` (3 moedas)
    - **Solução Ótima:** `3 + 3` (2 moedas)
- **Complexidade de Tempo:**
  - **Big O:** `O(n log n)` (dominado pela ordenação)
  - **Big Omega (Ω):** `Ω(n log n)`
  - **Big Theta (Θ):** `Θ(n log n)`

### Função 2: Recursiva Pura (Ingênua) - `qtdeMoedasRec`
- **Conceito:** Esta é uma abordagem de força bruta que explora todas as combinações possíveis de moedas. Para cada montante, a função testa subtrair cada moeda e chama a si mesma recursivamente para o valor restante, retornando o mínimo encontrado.
- **Análise de Desempenho 🐢:** A árvore de recursão cresce exponencialmente. Por exemplo, para `M=5` e `moedas=[1,2,3]`, o subproblema `M=2` seria calculado múltiplas vezes. Este reprocessamento torna a função extremamente lenta para valores de `M` moderados.
- **Complexidade de Tempo:**
  - **Big O:** `O(k^M)`, onde `k` é o número de moedas.
  - **Big Omega (Ω):** `Ω(M / c_max)`
  - **Big Theta (Θ):** `Θ(k^M)`

### Função 3: Recursiva com Memoização (Top-Down) - `qtdeMoedasRecMemo`
- **Conceito:** Esta abordagem otimiza a função recursiva pura usando **memoização**. Antes de calcular a solução para um montante `m`, a função verifica se o resultado já foi calculado e armazenado em um dicionário (`memo`). Se sim, retorna o valor salvo; caso contrário, calcula, armazena e retorna.
- **Ligação com a PD:** A memoização é uma forma de Programação Dinâmica conhecida como **Top-Down**, pois resolve o problema "de cima para baixo", partindo do `M` original e decompondo-o em subproblemas menores.
- **Melhoria na Eficiência ⚡:** A memoização elimina o reprocessamento, garantindo que cada subproblema seja resolvido apenas uma vez. Isso reduz drasticamente a complexidade de tempo.
- **Complexidade de Tempo:**
  - **Big O:** `O(M * k)`
  - **Big Omega (Ω):** `Ω(M)`
  - **Big Theta (Θ):** `Θ(M * k)`

### Função 4: Programação Dinâmica (Bottom-Up) - `qtdeMoedasPD`
- **Conceito:** Também conhecida como **tabulação**, esta abordagem constrói a solução de "baixo para cima". Ela cria um array `dp` de tamanho `M+1`, onde `dp[i]` armazena a quantidade mínima de moedas para formar o valor `i`. O array é preenchido iterativamente, começando de `i=1` até `M`.
- **Fluxo do Algoritmo:** Para cada `i`, a solução `dp[i]` é calculada usando os resultados já armazenados para valores menores (`dp[i - moeda]`).
- **Vantagem sobre Memoização:** A abordagem Bottom-Up evita a sobrecarga de chamadas recursivas, podendo ter uma pequena vantagem de desempenho em algumas implementações de Python.
- **Complexidade de Tempo:**
  - **Big O:** `O(M * k)`
  - **Big Omega (Ω):** `Ω(M)`
  - **Big Theta (Θ):** `Θ(M * k)`

---

## 3. Conclusão 🎯

### Resumo Comparativo de Complexidades

| Abordagem | Complexidade de Tempo (Θ) | Garante Solução Ótima? |
| :---------------- | :-----------------------: | :----------------------: |
| **Guloso** | `Θ(n log n)` | Não ❌ |
| **Recursivo Puro** | `Θ(k^M)` | Sim ✅ |
| **Memoização (Top-Down)** | `Θ(M * k)` | Sim ✅ |
| **PD (Bottom-Up)** | `Θ(M * k)` | Sim ✅ |

### Escolha Ótima 🏆
O algoritmo mais eficiente e robusto para resolver o Problema da Troca de Moedas é a **Programação Dinâmica (Bottom-Up)** ou a **Recursão com Memoização (Top-Down)**. Ambos garantem a solução ótima com uma complexidade de tempo pseudo-polinomial (`Θ(M * k)`), sendo viáveis para valores de `M` muito maiores do que a abordagem recursiva pura suportaria.

### Reflexão
Este desafio demonstra a importância de escolher o algoritmo correto. Enquanto uma abordagem gulosa é simples e rápida, sua incapacidade de garantir a otimalidade a torna inadequada para o problema geral. Por outro lado, a força bruta recursiva, embora correta, é computacionalmente inviável. A Programação Dinâmica surge como a solução ideal, equilibrando corretude e eficiência ao explorar a subestrutura do problema e eliminar redundâncias.
