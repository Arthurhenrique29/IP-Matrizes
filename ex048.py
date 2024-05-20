#Escreva um código que imprima uma matriz 5x5 com as duas diagonais com números 1 e o restante da matriz com 0, exceto pelo número central que deve ser 3.
matriz = []
for i in range(5):
    lista = []
    for j in range(5):
        if i == j or i == 5 - 1 - j:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
matriz[2][2] = 3
print('Matriz gerada:')
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=" ")
    print()

