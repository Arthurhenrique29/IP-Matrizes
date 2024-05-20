#Escreva um programa que receba duas tuplas como entrada e retorne uma nova tupla contendo todos os elementos das duas tuplas, sem repetições.
lista1 = input('Digite uma lista de números separados por espaço para a tupla 1: ').split()
lista1 = [int(i) for i in lista1]
tupla1 = ()
for i in lista1:
    tupla1 += (i,)
lista2 = input('Digite uma lista de números separados por espaço para a tupla 2: ').split()
lista2 = [int(i) for i in lista2]
tupla2 = ()
for i in lista2:
    tupla2 += (i,)
nova_tupla = ()
for i in tupla1:
    if i not in nova_tupla:
        nova_tupla += (i,)
for i in tupla2:
    if i not in nova_tupla:
        nova_tupla += (i,)
print('A nova tupla contento todos os elementos das duas tuplas é:')
print(nova_tupla)
