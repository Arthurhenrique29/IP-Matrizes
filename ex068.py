#Crie um programa que receba uma matriz como entrada e retorne duas listas, uma com a soma dos elementos de cada linha e outra com a soma dos elementos de cada coluna.
num_linhas = int(input('Digite o número de linhas da matriz: '))
num_colunas = int(input('Digite o número de colulas da matriz: '))
matriz = []
for i in range(num_linhas):
    linha = input(f'Digite os elementos da linha {i + 1} separados por espaço: ').split()
    linha = [int(i) for i in linha]
    matriz.append(linha)
soma_linhas = [0] * num_linhas
soma_colunas = [0] * num_colunas
for i in range(num_linhas):
    for j in range(num_colunas):
        soma_linhas[i] += matriz[i][j]
        soma_colunas[j] += matriz[i][j]
print('A soma dos elementos de cada linha: ', soma_linhas)
print('A soma dos elementos de cada coluna: ', soma_colunas)
