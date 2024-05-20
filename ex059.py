#Escreva um algoritmo que receba duas matrizes como entrada e retorne a soma dessas matrizes, desde que tenham as mesmas dimensões.
n = int(input('Digite o tamanho da matriz: Ex 3 para (3x3) '))
print('Digite os valores da primeira matriz:')
matriz1 = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz1.append(linha)
print('Digite os valores da segunda matriz:')
matriz2 = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz2.append(linha)
matriz_soma = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = matriz1[i][j] + matriz2[i][j]
        linha.append(valor)
    matriz_soma.append(linha)
print('A soma entre as matrizes é igual:')
for i in range(n):
    for j in range(n):
        print(matriz_soma[i][j], end=" ")
    print()
