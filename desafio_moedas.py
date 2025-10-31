import time

# =============================================================================
# CÓDIGO 1 - ALGORITMO GULOSO (GREEDY)
# =============================================================================
def qtdeMoedas(m, moedas):
    """
    Calcula a quantidade de moedas usando a estratégia gulosa.

    Args:
        m (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas disponíveis.

    Returns:
        int: A quantidade de moedas utilizadas. Retorna -1 se o montante não puder
             ser formado com as moedas fornecidas.

    Complexidade:
        - Tempo: O(n log n) devido à ordenação. A iteração é O(n).
        - Big O: O(n log n)
        - Big Omega (Ω): Ω(n log n)
        - Big Theta (Θ): Θ(n log n)
    """
    moedas.sort(reverse=True)
    qtd = 0
    m_restante = m
    
    for moeda in moedas:
        if m_restante == 0:
            break
        count = m_restante // moeda
        if count > 0:
            qtd += count
            m_restante -= count * moeda
            
    return qtd if m_restante == 0 else -1

# =============================================================================
# CÓDIGO 2 - RECURSIVO PURO (FORÇA BRUTA)
# =============================================================================
def qtdeMoedasRec(m, moedas):
    """
    Calcula a menor quantidade de moedas usando recursão pura (força bruta).

    Args:
        m (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas disponíveis.

    Returns:
        int: A quantidade mínima de moedas. Retorna -1 se for impossível.

    Complexidade:
        - Tempo: Exponencial, O(k^m), onde k é o número de moedas.
        - Big O: O(k^m)
        - Big Omega (Ω): Ω(m/c_max) no melhor cenário.
        - Big Theta (Θ): Θ(k^m)
    """
    if m == 0:
        return 0
    if m < 0:
        return float('inf')

    min_moedas = float('inf')
    
    for moeda in moedas:
        res = qtdeMoedasRec(m - moeda, moedas)
        if res != float('inf'):
            min_moedas = min(min_moedas, res + 1)
            
    return min_moedas if min_moedas != float('inf') else -1

# =============================================================================
# CÓDIGO 3 - RECURSIVO COM MEMOIZAÇÃO (TOP-DOWN)
# =============================================================================
def qtdeMoedasRecMemo(m, moedas, memo=None):
    """
    Calcula a menor quantidade de moedas usando recursão com memoização (Top-Down).

    Args:
        m (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas disponíveis.
        memo (dict): Dicionário para armazenar resultados de subproblemas.

    Returns:
        int: A quantidade mínima de moedas. Retorna -1 se for impossível.

    Complexidade:
        - Tempo: O(m * k), onde k é o número de moedas.
        - Big O: O(m * k)
        - Big Omega (Ω): Ω(m)
        - Big Theta (Θ): Θ(m * k)
    """
    if memo is None:
        memo = {}
    if m in memo:
        return memo[m]
    if m == 0:
        return 0
    if m < 0:
        return float('inf')

    min_moedas = float('inf')
    
    for moeda in moedas:
        res = qtdeMoedasRecMemo(m - moeda, moedas, memo)
        if res != float('inf'):
            min_moedas = min(min_moedas, res + 1)
            
    memo[m] = min_moedas
    return min_moedas if min_moedas != float('inf') else -1

# =============================================================================
# CÓDIGO 4 - PROGRAMAÇÃO DINÂMICA (BOTTOM-UP)
# =============================================================================
def qtdeMoedasPD(m, moedas):
    """
    Calcula a menor quantidade de moedas usando programação dinâmica (Bottom-Up).

    Args:
        m (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas disponíveis.

    Returns:
        int: A quantidade mínima de moedas. Retorna -1 se for impossível.

    Complexidade:
        - Tempo: O(m * k), onde k é o número de moedas.
        - Big O: O(m * k)
        - Big Omega (Ω): Ω(m)
        - Big Theta (Θ): Θ(m * k)
    """
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    
    for i in range(1, m + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)
                
    return int(dp[m]) if dp[m] != float('inf') else -1

# =============================================================================
# TESTES E COMPARAÇÃO
# =============================================================================
valor_teste = 35
moedas_teste = [1, 3, 4]

print(f"Executando testes para M = {valor_teste} com moedas {moedas_teste}")

# Teste 1: Guloso
inicio = time.time()
res1 = qtdeMoedas(valor_teste, moedas_teste.copy())
fim = time.time()
print(f"\n--- Estratégia Gulosa (qtdeMoedas) ---")
print(f"Resultado: {res1} moedas")
print(f"Tempo: {fim - inicio:.10f} s")

# Teste 2: Recursivo Puro
inicio = time.time()
res2 = qtdeMoedasRec(valor_teste, moedas_teste)
fim = time.time()
print(f"\n--- Recursivo Puro (qtdeMoedasRec) ---")
print(f"Resultado: {res2} moedas")
print(f"Tempo: {fim - inicio:.10f} s (Pode ser muito lento)")

# Teste 3: Memoização
inicio = time.time()
res3 = qtdeMoedasRecMemo(valor_teste, moedas_teste)
fim = time.time()
print(f"\n--- Memoização Top-Down (qtdeMoedasRecMemo) ---")
print(f"Resultado: {res3} moedas")
print(f"Tempo: {fim - inicio:.10f} s")

# Teste 4: PD Bottom-Up
inicio = time.time()
res4 = qtdeMoedasPD(valor_teste, moedas_teste)
fim = time.time()
print(f"\n--- PD Bottom-Up (qtdeMoedasPD) ---")
print(f"Resultado: {res4} moedas")
print(f"Tempo: {fim - inicio:.10f} s")