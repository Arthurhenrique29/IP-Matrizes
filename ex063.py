#Escreva um programa que ordene uma lista de números de forma que os números pares fiquem antes dos números ímpares, mantendo a ordem original dentro de cada grupo.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
for i in range(1, len(pares)):
    chave = pares[i]
    j = i - 1
    while j >= 0 and pares[j] > chave:
        pares[j + 1] = pares[j]
        j -= 1
    pares[j + 1] = chave
for i in range(1, len(impares)):
    chave = impares[i]
    j = i - 1
    while j >= 0 and impares[j] > chave:
        impares[j + 1] = impares[j]
        j -= 1
    impares[j + 1] = chave
lista_ord = pares + impares
print('Lista ordenada com pares antes dos ímpares:')
print(lista_ord)

