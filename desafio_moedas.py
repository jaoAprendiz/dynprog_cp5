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
    moedas.sort(reverse=True)  # Ordena moedas em ordem decrescente
    qtd = 0                     # Contador de moedas utilizadas
    pos = 0                     # Posição atual na lista de moedas
    
    # Percorre enquanto ainda há valor restante e moedas disponíveis
    while m > 0 and pos < len(moedas):
        if m >= moedas[pos]:
            qtd += 1            # Incrementa contador
            m = m - moedas[pos] # Subtrai valor da moeda
        else:
            pos += 1            # Passa para próxima moeda (menor)
    
    return qtd

# PRINTS DE TESTE - CÓDIGO 1
print("=" * 70)
print("CÓDIGO 1 - ALGORITMO GULOSO")
print("=" * 70)

print("Teste 1: qtdMoedas(17, [5, 2, 1])")
inicio = time.time()
resultado = qtdMoedas(17, [5, 2, 1])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 2: qtdMoedas(6, [1, 3, 4])")
inicio = time.time()
resultado = qtdMoedas(6, [1, 3, 4])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 3: qtdMoedas(11, [1, 5, 6])")
inicio = time.time()
resultado = qtdMoedas(11, [1, 5, 6])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print("(Guloso pode não dar resultado ótimo!)\n")

print("🎯 TESTE COM 35 MOEDAS: qtdMoedas(35, [1, 5, 10, 25])")
inicio = time.time()
resultado = qtdMoedas(35, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")


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
    menor = float('INF')  # Inicializa com infinito para encontrar o mínimo
    
    # Caso base: se valor é 0 ou negativo, não precisa de moedas
    if m <= 0: 
        return 0
    
    # Testa todas as moedas possíveis
    for moeda in moedas:
        if m >= moeda:  # Verifica se a moeda cabe no valor restante
            # Chama recursivamente para o valor restante
            qtde = qtdeNotasRec(m - moeda, moedas)
            # Atualiza o mínimo se encontrou solução melhor
            if qtde < menor:
                menor = qtde
    
    # Retorna mínimo + 1 (a moeda atual)
    return menor + 1    

# PRINTS DE TESTE - CÓDIGO 2
print("\n" + "=" * 70)
print("CÓDIGO 2 - RECURSIVO (FORÇA BRUTA)")
print("=" * 70)

print("Teste 1: qtdeNotasRec(17, [5, 2, 1])")
inicio = time.time()
resultado = qtdeNotasRec(17, [5, 2, 1])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print("# Resposta = 4 (três notas de 5 e uma de 2)\n")

print("Teste 2: qtdeNotasRec(6, [1, 3, 4])")
inicio = time.time()
resultado = qtdeNotasRec(6, [1, 3, 4])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 3: qtdeNotasRec(11, [1, 5, 6])")
inicio = time.time()
resultado = qtdeNotasRec(11, [1, 5, 6])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("🎯 TESTE COM 35 MOEDAS: qtdeNotasRec(35, [1, 5, 10, 25])")
print("⚠️  ATENÇÃO: Este teste pode demorar MUITO devido à complexidade exponencial!")
inicio = time.time()
resultado = qtdeNotasRec(35, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")


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

def qtdeNotasRecMemo(valor, moedas):
    """
    Calcula quantidade MÍNIMA de moedas usando recursão com memoização.
    
    Args:
        valor: valor a ser trocado
        moedas: lista de valores de moedas disponíveis
    
    Returns:
        quantidade mínima de moedas necessárias
    """
    # Caso base: valor 0 ou negativo não precisa de moedas
    if valor <= 0: 
        return 0
    
    # Se já calculamos este valor antes, retorna resultado armazenado
    if (valor in memo):
        return memo[valor]
    
    qtdeM = float('inf')  # Inicializa com infinito para encontrar mínimo
    
    # Testa todas as moedas possíveis
    for moeda in moedas:
        if valor >= moeda:  # Verifica se a moeda cabe no valor
            # Chamada recursiva para valor restante
            qtde = qtdeNotasRecMemo(valor - moeda, moedas)
            # Atualiza mínimo se encontrou solução melhor
            if qtde < qtdeM:
                qtdeM = qtde
    
    # Armazena resultado no memo antes de retornar
    memo[valor] = qtdeM + 1
    return qtdeM + 1

# PRINTS DE TESTE - CÓDIGO 3
print("\n" + "=" * 70)
print("CÓDIGO 3 - RECURSIVO COM MEMOIZAÇÃO")
print("=" * 70)

memo = {}
print("Teste 1: qtdeNotasRecMemo(17, [5, 2, 1])")
inicio = time.time()
resultado = qtdeNotasRecMemo(17, [5, 2, 1])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print(f"Subproblemas resolvidos: {len(memo)}")
print(f"Memo: {memo}\n")

memo = {}  # Limpa memo para novo teste
print("Teste 2: qtdeNotasRecMemo(6, [1, 3, 4])")
inicio = time.time()
resultado = qtdeNotasRecMemo(6, [1, 3, 4])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print(f"Subproblemas resolvidos: {len(memo)}")
print(f"Memo: {memo}\n")

memo = {}  # Limpa memo para novo teste
print("Teste 3: qtdeNotasRecMemo(100, [1, 5, 10, 25])")
inicio = time.time()
resultado = qtdeNotasRecMemo(100, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print(f"Subproblemas resolvidos: {len(memo)}\n")

memo = {}  # Limpa memo para novo teste
print("🎯 TESTE COM 35 MOEDAS: qtdeNotasRecMemo(35, [1, 5, 10, 25])")
inicio = time.time()
resultado = qtdeNotasRecMemo(35, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos")
print(f"Subproblemas resolvidos: {len(memo)}")
print(f"Memo: {memo}\n")


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
    # Cria array memo com tamanho m+1, inicializado com infinito
    memo = [float('inf')] * (m + 1)
    memo[0] = 0  # Caso base: 0 reais precisa de 0 moedas
    
    pos = 1  # Começa do valor 1
    
    # Itera de 1 até m, calculando mínimo para cada valor
    while pos <= m:
        # Para cada valor, testa todas as moedas disponíveis
        for moeda in moedas:
            if moeda <= pos:  # Se a moeda cabe no valor atual
                # Atualiza com mínimo entre: valor atual OU usar esta moeda
                # memo[pos-moeda] é o mínimo para o valor restante
                memo[pos] = min(memo[pos], memo[pos-moeda]) + 1
        pos += 1
    
    return memo[m]  # Retorna resultado final para valor m

# PRINTS DE TESTE - CÓDIGO 4
print("\n" + "=" * 70)
print("CÓDIGO 4 - PROGRAMAÇÃO DINÂMICA (BOTTOM-UP)")
print("=" * 70)

print("Teste 1: qtdmoedaspd(6, [1, 3, 4])")
inicio = time.time()
resultado = qtdmoedaspd(6, [1, 3, 4])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 2: qtdmoedaspd(17, [5, 2, 1])")
inicio = time.time()
resultado = qtdmoedaspd(17, [5, 2, 1])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 3: qtdmoedaspd(11, [1, 5, 6])")
inicio = time.time()
resultado = qtdmoedaspd(11, [1, 5, 6])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("Teste 4: qtdmoedaspd(100, [1, 5, 10, 25])")
inicio = time.time()
resultado = qtdmoedaspd(100, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")

print("🎯 TESTE COM 35 MOEDAS: qtdmoedaspd(35, [1, 5, 10, 25])")
inicio = time.time()
resultado = qtdmoedaspd(35, [1, 5, 10, 25])
fim = time.time()
print(f"Resultado: {resultado} moedas")
print(f"Tempo de execução: {fim - inicio:.10f} segundos\n")
