#Desenvolva um programa que calcule a soma dos elementos das diagonais principal e secundária de uma matriz.
n = int(input('Digite o número de linhas e colunas de uma matriz quadrada: '))
matriz = []
for i in range(n):
    linha = input(f'Digite os elementos da linha {i + 1} separados por espaço: ').split()
    linha = [int(i) for i in linha]
    matriz.append(linha)
print('Matriz:')
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()
diag1 = 0
diag2 = 0
for i in range(n):
    diag1 += matriz[i][i]
    diag2 += matriz[i][n -1 -i]
print('Soma dos elementos da diagonal principal:', diag1)
print('Soma dos elementos da diagonal secundária:', diag2)