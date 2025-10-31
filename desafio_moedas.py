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
        int: A quantidade de moedas, que não é garantidamente a mínima.
        
    Complexidade:
        - Tempo: O(n log n) devido à ordenação.
    """
    moedas.sort(reverse=True)
    qtd = 0
    pos = 0
    while m > 0 and pos < len(moedas):
        if m >= moedas[pos]:
            qtd += 1
            m = m - moedas[pos]
        else:
            pos += 1
    return qtd

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
        int: A quantidade mínima de moedas.
        
    Complexidade:
        - Tempo: Exponencial, O(k^m), onde k é o número de moedas.
    """
    menor = float('INF')
    if m <= 0:
        return 0
    for moeda in moedas:
        if m >= moeda:
            qtde = qtdeMoedasRec(m - moeda, moedas)
            if qtde < menor:
                menor = qtde
    return menor + 1

# =============================================================================
# CÓDIGO 3 - RECURSIVO COM MEMOIZAÇÃO (TOP-DOWN)
# =============================================================================
memo = {} # A variável memo é global, conforme o código original
def qtdeMoedasRecMemo(valor, moedas):
    """
    Calcula a menor quantidade de moedas com recursão e memoização.

    Args:
        valor (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas.

    Returns:
        int: A quantidade mínima de moedas.
        
    Complexidade:
        - Tempo: O(m * k), onde k é o número de moedas.
    """
    if valor <= 0:
        return 0
    if valor in memo:
        return memo[valor]
    
    qtdeM = float('inf')
    for moeda in moedas:
        if valor >= moeda:
            qtde = qtdeMoedasRecMemo(valor - moeda, moedas)
            if qtde < qtdeM:
                qtdeM = qtde
    
    memo[valor] = qtdeM + 1
    return qtdeM + 1

# =============================================================================
# CÓDIGO 4 - PROGRAMAÇÃO DINÂMICA (BOTTOM-UP)
# =============================================================================
def qtdeMoedasPD(m, moedas):
    """
    Calcula a menor quantidade de moedas usando programação dinâmica (Bottom-Up).

    Args:
        m (int): O montante a ser trocado.
        moedas (list): Uma lista de inteiros com os valores das moedas.

    Returns:
        int: A quantidade mínima de moedas.
        
    Complexidade:
        - Tempo: O(m * k), onde k é o número de moedas.
    """
    memo_pd = [float('inf')] * (m + 1)
    memo_pd[0] = 0
    pos = 1
    while pos <= m:
        for moeda in moedas:
            if moeda <= pos:
                memo_pd[pos] = min(memo_pd[pos], memo_pd[pos - moeda] + 1)
        pos += 1
    return int(memo_pd[m])

# =============================================================================
# TESTES E COMPARAÇÃO
# =============================================================================
valor_teste = 35
moedas_teste = [1, 3, 4]

print(f"Executando testes para M = {valor_teste} com moedas {moedas_teste}\n")

# --- Teste 1: Guloso ---
inicio = time.time()
res1 = qtdeMoedas(valor_teste, moedas_teste.copy())
fim = time.time()
print(f"--- Estratégia Gulosa (qtdeMoedas) ---")
print(f"Resultado: {res1} moedas")
print(f"Tempo: {fim - inicio:.15f} s\n")

# --- Teste 2: Recursivo Puro ---
inicio = time.time()
res2 = qtdeMoedasRec(valor_teste, moedas_teste)
fim = time.time()
print(f"--- Recursivo Puro (qtdeMoedasRec) ---")
print(f"Resultado: {res2} moedas")
print(f"Tempo: {fim - inicio:.15f} s\n")

# --- Teste 3: Memoização ---
memo.clear()
inicio = time.time()
res3 = qtdeMoedasRecMemo(valor_teste, moedas_teste)
fim = time.time()
print(f"--- Memoização Top-Down (qtdeMoedasRecMemo) ---")
print(f"Resultado: {res3} moedas")
print(f"Tempo: {fim - inicio:.15f} s\n")

# --- Teste 4: PD Bottom-Up ---
inicio = time.time()
res4 = qtdeMoedasPD(valor_teste, moedas_teste)
fim = time.time()
print(f"--- PD Bottom-Up (qtdeMoedasPD) ---")
print(f"Resultado: {res4} moedas")
print(f"Tempo: {fim - inicio:.15f} s")
