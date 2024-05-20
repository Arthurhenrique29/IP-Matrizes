#Escreva um programa que receba uma tupla e conte quantos elementos únicos ela possui.
lista1 = input('Digite uma lista de números separados por espaço para a tupla 1: ').split()
lista1 = [int(i) for i in lista1]
tupla1 = ()
for i in lista1:
    tupla1 += (i,)
unicos =[]
cont = 0
for i in tupla1:
    if i not in unicos:
        unicos.append(i)
        cont += 1
print(f'A quantida de elementos únicos é {cont}.')