#Desenvolva um programa que remova todos os elementos ímpares de uma lista e imprima a lista resultante.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
print('Os elementos da lista são:', lista)
x = 0
while x < len(lista):
    if lista[x] % 2 != 0:
        del lista[x]
    else:
        x += 1
print('Lista de números após remover os ímpares: ', lista)