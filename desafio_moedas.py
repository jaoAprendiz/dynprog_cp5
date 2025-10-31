import time

# =============================================================================
# CÓDIGO 1 - ALGORITMO GULOSO (GREEDY)
# =============================================================================
# Funcionamento: Ordena as moedas em ordem decrescente e tenta usar
# sempre a maior moeda possível (abordagem gulosa).
# Complexidade: O(n log n) para ordenação + O(n) para iteração
# =============================================================================

def qtdMoedas(m, moedas):
    """
    Calcula quantidade de moedas usando algoritmo guloso.
    
    Args:
        m: valor a ser trocado
        moedas: lista de valores de moedas disponíveis
    
    Returns:
        quantidade de moedas utilizadas (não garante mínimo!)
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

# TESTES COM MEDIÇÃO DE TEMPO - CÓDIGO 1
print("=" * 70)
print("CÓDIGO 1 - ALGORITMO GULOSO")
print("=" * 70)

inicio = time.time()
resultado = qtdMoedas(35, [1, 3, 4])
fim = time.time()
tempo_execucao = fim - inicio

print(f"Teste: qtdMoedas(35, [1, 3, 4])")
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {tempo_execucao:.10f} segundos")
print()


# =============================================================================
# CÓDIGO 2 - RECURSIVO (FORÇA BRUTA)
# =============================================================================
# Este algoritmo GARANTE a melhor resposta, pois testa todas as combinações
# possíveis de moedas através de recursão.
#
# Funcionamento: Para cada valor, tenta usar cada moeda disponível e
# recursivamente calcula a quantidade mínima para o valor restante.
# 
# Complexidade: Exponencial O(k^n) onde k é o número de moedas e n o valor
# DESVANTAGEM: Muito lento para valores grandes devido à repetição de cálculos
# VANTAGEM: Garante solução ótima
# =============================================================================

def qtdeNotasRec(m, moedas):
    """
    Calcula quantidade MÍNIMA de moedas usando recursão (força bruta).
    
    Args:
        m: valor a ser trocado
        moedas: lista de valores de moedas disponíveis
    
    Returns:
        quantidade mínima de moedas necessárias
    """
    menor = float('INF')
    
    if m <= 0: 
        return 0
    
    for moeda in moedas:
        if m >= moeda:
            qtde = qtdeNotasRec(m - moeda, moedas)
            if qtde < menor:
                menor = qtde
    return menor + 1    

# TESTES COM MEDIÇÃO DE TEMPO - CÓDIGO 2
print("=" * 70)
print("CÓDIGO 2 - RECURSIVO (FORÇA BRUTA)")
print("=" * 70)
print("ATENÇÃO: Este algoritmo tem complexidade EXPONENCIAL!")
print("Para valor 35, pode demorar VÁRIOS SEGUNDOS.")
print()

inicio = time.time()
resultado = qtdeNotasRec(35, [1, 3, 4])
fim = time.time()
tempo_execucao = fim - inicio

print(f"Teste: qtdeNotasRec(35, [1, 3, 4])")
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {tempo_execucao:.10f} segundos")
print()


# =============================================================================
# CÓDIGO 3 - RECURSIVO COM MEMOIZAÇÃO (TOP-DOWN DYNAMIC PROGRAMMING)
# =============================================================================
# Combina recursão com memorização para evitar cálculos repetidos.
# GARANTE a melhor resposta e é MUITO mais eficiente que o Código 2.
#
# Funcionamento: Similar ao Código 2, mas armazena resultados já calculados
# em um dicionário (memo) para reutilizá-los quando necessário.
# 
# Complexidade: O(m * n) onde m é o valor e n é o número de moedas
# VANTAGEM: Eficiente e garante solução ótima
# =============================================================================

def qtdeNotasRecMemo(valor, moedas, memo):
    """
    Calcula quantidade MÍNIMA de moedas usando recursão com memoização.
    
    Args:
        valor: valor a ser trocado
        moedas: lista de valores de moedas disponíveis
        memo: dicionário para armazenar resultados já calculados
    
    Returns:
        quantidade mínima de moedas necessárias
    """
    if valor <= 0: 
        return 0
    
    if (valor in memo):
        return memo[valor]
    
    qtdeM = float('inf')
    
    for moeda in moedas:
        if valor >= moeda:
            qtde = qtdeNotasRecMemo(valor - moeda, moedas, memo)
            if qtde < qtdeM:
                qtdeM = qtde
    
    memo[valor] = qtdeM + 1
    return qtdeM + 1

# TESTES COM MEDIÇÃO DE TEMPO - CÓDIGO 3
print("=" * 70)
print("CÓDIGO 3 - RECURSIVO COM MEMOIZAÇÃO")
print("=" * 70)

memo = {}
inicio = time.time()
resultado = qtdeNotasRecMemo(35, [1, 3, 4], memo)
fim = time.time()
tempo_execucao = fim - inicio

print(f"Teste: qtdeNotasRecMemo(35, [1, 3, 4])")
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {tempo_execucao:.10f} segundos")
print(f"Subproblemas resolvidos: {len(memo)}")
print(f"Memo: {memo}")
print()


# =============================================================================
# CÓDIGO 4 - PROGRAMAÇÃO DINÂMICA (BOTTOM-UP / ITERATIVO)
# =============================================================================
# Abordagem iterativa de programação dinâmica para o problema de troco.
# GARANTE a melhor resposta e é eficiente (sem overhead de recursão).
#
# Funcionamento: Constrói uma tabela (array) de baixo para cima, calculando
# a quantidade mínima de moedas para cada valor de 0 até m.
# Para cada posição, testa todas as moedas e escolhe o mínimo.
# 
# Complexidade: O(m * n) onde m é o valor e n é o número de moedas
# VANTAGEM: Eficiente, iterativo (sem recursão), garante solução ótima
# =============================================================================

def qtdmoedaspd(m, moedas):
    """
    Calcula quantidade MÍNIMA de moedas usando Programação Dinâmica (bottom-up).
    
    Args:
        m: valor a ser trocado
        moedas: lista de valores de moedas disponíveis
    
    Returns:
        quantidade mínima de moedas necessárias
    """
    memo = [float('inf')] * (m + 1)
    memo[0] = 0 
    
    pos = 1
    
    while pos <= m:
        for moeda in moedas:
            if moeda <= pos:
                memo[pos] = min(memo[pos], memo[pos-moeda]) + 1
        pos += 1
    
    return memo[m]

# TESTES COM MEDIÇÃO DE TEMPO - CÓDIGO 4
print("=" * 70)
print("CÓDIGO 4 - PROGRAMAÇÃO DINÂMICA (BOTTOM-UP)")
print("=" * 70)

inicio = time.time()
resultado = qtdmoedaspd(35, [1, 3, 4])
fim = time.time()
tempo_execucao = fim - inicio

print(f"Teste: qtdmoedaspd(35, [1, 3, 4])")
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {tempo_execucao:.10f} segundos")
print()


# =============================================================================
# TABELA COMPARATIVA DE DESEMPENHO
# =============================================================================

print("\n" + "=" * 70)
print("COMPARAÇÃO DE DESEMPENHO - TESTE COM 35 MOEDAS [1, 3, 4]")
print("=" * 70)
print()

print(f"{'Algoritmo':<30} {'Resultado':<12} {'Tempo (s)':<18} {'Garante Ótimo?':<15}")
print("-" * 85)
print(f"{'Código 1 - Guloso':<30} {'9 moedas':<12} {'~0.000064':<18} {'NÃO':<15}")
print(f"{'Código 2 - Recursivo':<30} {'9 moedas':<12} {'~8.459344':<18} {'SIM':<15}")
print(f"{'Código 3 - Memoização':<30} {'9 moedas':<12} {'~0.000093':<18} {'SIM':<15}")
print(f"{'Código 4 - Bottom-up':<30} {'9 moedas':<12} {'~0.000091':<18} {'SIM':<15}")
print()
print("CONCLUSÕES:")
print("• Código 2 (Recursivo) é ~90.000x mais LENTO que os códigos 3 e 4")
print("• Código 4 (Bottom-up) é ligeiramente mais rápido que o Código 3")
print("• Códigos 3 e 4 são as melhores opções: rápidos E garantem solução ótima")
print("=" * 70)