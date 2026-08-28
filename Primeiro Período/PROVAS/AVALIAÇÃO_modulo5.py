"""
Universidade Federal do Mato Grosso do Sul
Curso Superior em Inteligência Artificial
Professor: Aumary Júnior e Thiago Santiago
Aluno: Saulo Ferro Maciel

MODULO 5 CHECKOUT
TAREFA 1 - Depuração e Documentação de Programas
"""


def p01(anterior, atual):
    """
    Problema 1 - Consumo de Água.
    Calcula o consumo (em m³) a partir da leitura anterior e da leitura
    atual do hidrômetro (atual sempre >= anterior).
    """
    consumo = -1
    try:
        # Erro sintático no original: "int(input()" faltava fechar o parêntese.
        # Erro semântico: a leitura atual estava sendo lida como float, mas o
        # enunciado pede dois inteiros -> ambas as leituras convertidas para int.
        anterior = int(anterior)
        atual = int(atual)
    except ValueError: print("Erro: os parâmetros devem ser valores inteiros.")
    # Erro semântico: a conta original era "anterior - atual", invertida.
    # Como atual >= anterior, o correto é "atual - anterior".
    if atual >= anterior: consumo = atual - anterior
    # Erro de digitação: o print original usava a variável "consumos" (com "s"),
    # que nunca havia sido definida -> corrigido para "consumo".
    print(consumo)


def p02(tarifa_fixa, peso_carga, valor_quilograma):
    """
    Problema 2 - Frete de Entregas.
    Calcula o frete a partir da tarifa fixa, do peso da carga e do valor
    por quilograma: frete = tarifa_fixa + (peso_carga * valor_quilograma).
    """
    frete = -1.00
    try:
        # Erro sintático no original: "float(input()" faltava fechar o parêntese
        # na leitura do "valor" -> parênteses corrigidos nos três casts.
        tarifa_fixa = float(tarifa_fixa)
        peso_carga = float(peso_carga)
        valor_quilograma = float(valor_quilograma)
    except ValueError: print("Erro: os parâmetros devem ser valores numéricos (float).")
    if tarifa_fixa != 0 and peso_carga != 0 and valor_quilograma != 0 and tarifa_fixa >= 0 and peso_carga >= 0 and valor_quilograma >= 0:
        # Erro semântico: a fórmula original somava os três valores
        # (tarifa + peso + valor). O enunciado pede tarifa + (peso * valor).
        frete = float(f"{tarifa_fixa + peso_carga * valor_quilograma:.2f}")
    # Erro de digitação: o print original usava a variável "total", nunca
    # definida -> corrigido para "frete".
    print(f"{frete:.2f}")


def p03(iqa):
    """
    Problema 3 - Classificação da Qualidade do Ar.
    Classifica o IQA em "Boa" (<=50), "Moderada" (<=100), "Ruim" (<=150)
    ou "Muito ruim" (>150).
    """
    try: iqa = float(iqa)
    except ValueError: print("Erro: o parâmetro deve ser um valor numérico (float).")

    if iqa > 0 and iqa >= 0:
        # Erro sintático no original: "if iqa <= 50" sem os dois-pontos.
        # Erro semântico: os testes eram todos "if" independentes (não "elif"),
        # e os limites estavam errados (< 100 ao invés de <= 100, >= 150 na
        # linha de "Ruim" ao invés de <= 150), fazendo o "else" só considerar
        # a condição anterior. Corrigido para uma cadeia if/elif/else coerente
        # com a tabela do enunciado.
        # Erro de digitação: "Moderado" -> "Moderada" (conforme o enunciado).
        if iqa <= 50: print("Boa")
        elif iqa <= 100: print("Moderada")
        elif iqa <= 150: print("Ruim")
        else: print("Muito ruim")
    else: print(-1)


def p04(N, M=0, A=0):
    """
    Problema 4 - Controle de Estacionamento.
    Lê N registros de veículos ('M' para moto, 'A' para automóvel) e
    imprime o total de veículos, de motos e de automóveis.
    """
    transporte = -1
    try:
        N = int(N)
        M = int(M)
        A = int(A)
    except ValueError: print("Erro: os parâmetros devem ser valores inteiros.")

    if N != 0 and N > 0 and M == 0 and A == 0:
        # Erro sintático no original: "for i in range( n )" sem os dois-pontos.
        # Erro semântico (remanescente de uma versão anterior): o intervalo
        # estava como "range(0, N+1)", o que lê N+1 registros em vez de N
        # (e pode travar a leitura por faltar entrada) -> corrigido para "range(0, N)".
        for i in range(0, N):
            try: transporte = input()
            except ValueError: print("Erro: transporte deve ser uma string.")

            # Erro semântico (remanescente de uma versão anterior): a checagem
            # era "transporte.split() == ''", que nunca é verdadeira porque
            # .split() devolve uma lista, não uma string -> corrigido para
            # "transporte.strip() == ''", que detecta corretamente uma linha vazia.
            if transporte.strip() == "":
                print(-1)
                break

            # Erro sintático no original: "if t = 'm':" usava atribuição (=)
            # em vez de comparação (==) -> corrigido para "==" (via .lower()).
            # Erro de digitação/semântico: "auto =+ 1" incrementava com o
            # operador errado (equivale a "auto = +1") -> corrigido para "+=".
            if transporte[0].lower() == "m": M += 1
            elif transporte[0].lower() == "a": A += 1
            else:print("valor errado, apenas \"m\" e \"a\"")

        # Erro de digitação: o print original usava a variável "total", nunca
        # definida -> corrigido para exibir N, M e A com rótulos.
        print(f"Total de transportes: {N}\n Total de Motos: {M}\n Total de Automóveis: {A}")
    else:
        print(transporte)


def p05(N, MENOR=0, MAIOR=0):
    """
    Problema 5 - Monitoramento Climático.
    Lê N temperaturas e imprime a maior, a menor e a média.
    """
    temps = -1
    try:
        N = int(N)
    except ValueError: print("Erro: o parâmetro deve ser um valor inteiro.")

    if N != 0 and N > 0:
        # Erro sintático no original: "list(map(float, input().split())"
        # faltava fechar o parêntese -> parênteses corrigidos.
        temps = list(map(float, input().split()))

        if len(temps) == N:
            # Erro semântico: o original iniciava "maior = temps[1]" (pulava o
            # primeiro elemento e podia gerar IndexError se N==1) enquanto
            # "menor" partia de temps[0] -> ambos corrigidos para partir de temps[0].
            MAIOR = temps[0]
            MENOR = temps[0]
            soma = 0

            for t in temps:
                # Erro semântico: a comparação para "maior" usava "t < maior"
                # (lógica invertida) -> corrigido para "t > MAIOR".
                # Erro de digitação: "soma =+ t" (equivale a "soma = +t") em vez
                # de "soma += t" -> corrigido.
                if t > MAIOR: MAIOR = t
                if t < MENOR: MENOR = t
                soma += t

            print(f"{MAIOR:.1f}")
            print(f"{MENOR:.1f}")
            print(f"{soma / N:.2f}")
        else:
            print(-1)
    else:
        print(temps)


def p06(N, M):
    """
    Problema 6 - Mapa de Áreas Verdes.
    Lê um mapa de N linhas por M colunas (caracteres 'V' ou 'C') e conta
    quantas posições contêm vegetação ('V').
    """
    cont = -1
    try:
        # Erro sintático no original: "map(int, input().split()" faltava
        # fechar o parêntese -> corrigido.
        N = int(N)
        M = int(M)
    except ValueError: print("Erro: os parâmetros devem ser valores inteiros.")

    if N != 0 and M != 0 and N > 0 and M > 0:
        mapa = []
        for i in range(0, N):
            linha = input()
            mapa.append(linha)

        cont = 0
        # Erro semântico: o original percorria "for i in range(m): for j in
        # range(n): mapa[i][j]", trocando linhas por colunas (mapa tem N linhas
        # de M caracteres) -> corrigido percorrendo diretamente cada caractere
        # de cada linha, evitando também índice fora do intervalo quando N != M.
        # Erro semântico: comparava com "v" minúsculo, mas o enunciado usa "V"
        # maiúsculo -> corrigido para c.upper() == "V".
        # Erro de digitação: "cont =+ 1" -> corrigido para "cont += 1".
        for linha in mapa:
            for c in linha:
                if c.upper() == "V": cont += 1

    # Erro de digitação: o print original usava a variável "contagem", nunca
    # definida -> corrigido para "cont".
    print(cont)


def disponivel(total, emp):
    """
    Função auxiliar do Problema 7.
    Indica se um livro tem exemplar disponível: verdadeiro quando a
    quantidade emprestada é menor que a quantidade total de exemplares.
    """
    # Erro sintático no original: "def disponivel(total, emp)" sem os
    # dois-pontos.
    # Erro semântico: a condição original era "emp <= total", que é quase
    # sempre verdadeira (só falha se houver mais exemplares emprestados do
    # que o total, uma situação inconsistente) -> corrigido para "emp < total",
    # que reflete corretamente "sobrou pelo menos 1 exemplar".
    return emp < total


def p07(N):
    """
    Problema 7 - Sistema de Biblioteca.
    Lê N livros (título, total de exemplares, quantidade emprestada) e
    imprime o título de cada livro com exemplar disponível. Caso nenhum
    livro esteja disponível, imprime "Nenhum livro disponível".
    """
    resultado = -1
    try:
        N = int(N)
    except ValueError: print("Erro: o parâmetro deve ser um valor inteiro.")

    if N != 0 and N > 0:
        achou = False

        for i in range(0, N):
            titulo = input()
            total = int(input())
            emp = int(input())

            # Erro semântico: a chamada original era "disponivel(emp, total)",
            # com os argumentos trocados em relação à definição da função
            # "disponivel(total, emp)" -> corrigido para "disponivel(total, emp)".
            # Erro semântico: o original imprimia "total" (a quantidade de
            # exemplares) em vez do título do livro -> corrigido para "titulo",
            # conforme pede o enunciado.
            if disponivel(total, emp):
                print(titulo)
                achou = True

        # Erro semântico: a condição original era "if achou:", ou seja,
        # imprimia a mensagem de indisponibilidade justamente quando um livro
        # HAVIA sido encontrado -> lógica invertida, corrigida para "if not achou:".
        if not achou:
            print("Nenhum livro disponível")
    else:
        print(resultado)


def ler_matriz(l, p):
    """
    Função auxiliar do Problema 8.
    Lê 'l' linhas contendo 'p' inteiros cada (número de passageiros por
    parada em cada linha de ônibus) e retorna a matriz lida.
    """
    # Erro sintático no original: "for i in range( l )" sem os dois-pontos.
    mat = []
    for i in range(0, l):
        mat.append(list(map(int, input().split())))
    return mat


def total_linha(v):
    """
    Função auxiliar do Problema 8.
    Recebe uma lista de passageiros embarcados por parada em uma linha de
    ônibus e retorna o total de passageiros dessa linha.
    """
    s = 0
    # Erro de digitação: "s =+ x" (equivale a "s = +x") em vez de "s += x"
    # -> corrigido, senão a soma nunca acumulava os valores.
    for x in v: s += x
    return s


def melhor(mat):
    """
    Função auxiliar do Problema 8.
    Recebe a matriz de passageiros (uma linha de ônibus por linha da
    matriz) e retorna o índice e o total da linha mais movimentada.
    """
    idx = 0
    maior = total_linha(mat[0])

    for i in range(1, len(mat)):
        t = total_linha(mat[i])
        # Erro semântico: a comparação original era "t < maior" (lógica
        # invertida, buscava a linha com MENOS passageiros) -> corrigido
        # para "t > maior", que busca a linha mais movimentada.
        if t > maior:
            maior = t
            idx = i

    return idx, maior


def p08(L, P):
    """
    Problema 8 - Planejamento de Rotas de Ônibus.
    Lê L linhas de ônibus com P paradas cada, determina a linha mais
    movimentada e imprime seu número (1-based) e o total de passageiros.
    """
    resultado = -1
    try:
        L = int(L)
        P = int(P)
    except ValueError: print("Erro: os parâmetros devem ser valores inteiros.")

    if L != 0 and P != 0 and L > 0 and P > 0:
        # Erro semântico: a chamada original era "ler_matriz(p, l)", com os
        # argumentos invertidos em relação à definição "ler_matriz(l, p)"
        # (l = linhas de ônibus, p = paradas por linha) -> corrigido para
        # "ler_matriz(L, P)".
        mat = ler_matriz(L, P)
        linha, total = melhor(mat)

        # Erro de digitação: o print original usava a variável "linhas"
        # (com "s"), nunca definida -> corrigido para "linha + 1", exibindo
        # o número da linha no formato 1-based pedido pelo enunciado.
        print(linha + 1)
        print(total)
    else:
        print(resultado)