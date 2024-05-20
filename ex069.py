#Escreva um programa que substitua todos os elementos de uma matriz por um valor especificado pelo usuário.
num_linhas = int(input('Digite o número de linhas da matriz: '))
num_colunas = int(input('Digite o número de colulas da matriz: '))
matriz = []
for i in range(num_linhas):
    linha = input(f'Digite os elementos da linha {i + 1} separados por espaço: ').split()
    linha = [int(i) for i in linha]
    matriz.append(linha)
print('Primeira matriz:')
for i in range(num_linhas):
    for j in range(num_colunas):
        print(matriz[i][j], end=" ")
    print()
novo_valor = int(input('Digite o valor que substituirá todos os elementos da matriz: '))
for i in range(num_linhas):
    for j in range(num_colunas):
        matriz[i][j] = novo_valor
print('Nova Matriz:')
for i in range(num_linhas):
    for j in range(num_colunas):
        print(matriz[i][j], end=" ")
    print()