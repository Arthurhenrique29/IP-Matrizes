#Crie um programa que receba uma matriz como entrada e retorne uma lista com as médias de cada coluna.
num_linhas = int(input('Digite o número de linhas da matriz: '))
num_colunas = int(input('Digite o número de colulas da matriz: '))
matriz = []
for i in range(num_linhas):
    linha = input(f'Digite os elementos da linha {i + 1} separados por espaço: ').split()
    linha = [int(i) for i in linha]
    matriz.append(linha)
soma = [0] * num_colunas
for i in range(num_linhas):
    for j in range(num_colunas):
        soma[j] += matriz[i][j]
media = [i / num_linhas for i in soma]
print(f'A média das colunas é:', media)


