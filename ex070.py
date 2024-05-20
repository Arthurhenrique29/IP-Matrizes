#Escreva um programa que verifique se uma matriz é esparsa, ou seja, se a maioria dos seus elementos é zero.
num_linhas = int(input('Digite o número de linhas da matriz: '))
num_colunas = int(input('Digite o número de colulas da matriz: '))
matriz = []
for i in range(num_linhas):
    linha = input(f'Digite os elementos da linha {i + 1} separados por espaço: ').split()
    linha = [int(i) for i in linha]
    matriz.append(linha)
cont0 = 0
elementos = num_linhas * num_colunas
for i in range(num_linhas):
    for j in range(num_colunas):
        if matriz[i][j] == 0:
            cont0 += 1
if cont0 > elementos / 2:
    print('A matriz é esparsa.')
else:
    print('A matriz não é esparsa.')
