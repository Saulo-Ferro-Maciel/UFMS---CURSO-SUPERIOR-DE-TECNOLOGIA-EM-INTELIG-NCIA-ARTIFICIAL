# PRINCIPAIS VARIÁVEIS GLOBAIS
linhas = int(input("Qtd de linhas: "))
colunas = int(input("Qtd de colunas: "))
arvores = obstaculos = livres = 0
maior = linha_maior = percentual = -1
porcentagem, cordenadas, mapa = 0, [], []

# LOOP FOR QUE ALEM DE CAPTURAR AS LINHAS, VERIFICA SE EXISTE ARVORE NAS EXTREMIDADES
# REGISTRA AS COORDENADAS DAS ARVORES NAS EXTREMIDADES EM UMA LISTA
for i in range(linhas):
    linha = list(input(f"Digite a linha {i+1}: "))
    if linha[0] == "A" :
        arvore_borda = [f"Linha {i+1}", f"Coluna 0"]
        cordenadas.append(arvore_borda)
    if linha[-1] == "A":
        arvore_borda = [f"Linha {i+1}", f"Coluna {colunas-1}"]
        cordenadas.append(arvore_borda)
    mapa.append(linha)

for i in range(linhas):
    cont = 0
    for j in range(colunas):
        if mapa[i][j] == 'A':
            arvores += 1
            cont += 1
        elif mapa[i][j] == '#': obstaculos += 1
        else: livres += 1

    if cont > maior:
        maior = cont
        linha_maior = i

    # CALCULO DO PERCENTUAL DE ARVORES E CLASSIFICAÇÃO DE ARBORIZAÇÃO
    porcentagem = (cont*100)/colunas
    if porcentagem < 20: percentual = f"{porcentagem:.0f}% - pouco arborizado"
    elif porcentagem >= 20 and porcentagem < 50: percentual = f"{porcentagem:.0f}% - Arborização média"
    else: percentual = f"{porcentagem:.0f}% - Muito arborizado"
    
print(f"\nÁrvores: {arvores}")
print(f"Obstáculos: {obstaculos}")
print(f"Livres: {livres}")
print(f"Linha com mais árvores: {linha_maior}")
print(f"Percentual de árvores: {percentual}")

# IMPRESSÃO DAS COORDENADAS DAS ARVORES NAS EXTREMIDADES
print("Linhas com árvores nas extremidades:")
for coordenada in cordenadas:
    print(f"  {coordenada[0]} - {coordenada[1]}")