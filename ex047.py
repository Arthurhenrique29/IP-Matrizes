#Escreva um código que imprimirá uma matriz de um tamanho digitado pelo usuário.
import random
linhas = int(input('Digite o número de linhas da matriz: '))
colunas = int(input('Digite o número de colunas da matriz: '))
matriz = []
soma = 0
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.randint(1,9)
        linha.append(numero)
        soma += numero
    matriz.append(linha)
print('Matriz gerada:')
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end=' ')
    print()
media = soma / (linhas * colunas)
print(f'A soma de todos os números vale {soma}!')
print(f'A média de todos os números vale {media:.2f}')
